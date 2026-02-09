#!/usr/bin/env python3
import argparse
import os
import re
import sys

KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
XML_TAG_RE = re.compile(r"<[^>]+>")
RESERVED_WORDS = {"claude", "anthropic"}
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}


def parse_args():
    parser = argparse.ArgumentParser(description="Validate a skill directory.")
    parser.add_argument("skill_path", help="Path to a skill folder")
    return parser.parse_args()


def _strip_quotes(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        return value[1:-1]
    return value


def _parse_inline_list(value):
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    items = [item.strip() for item in inner.split(",")]
    return [_strip_quotes(item) for item in items if item]


def _parse_inline_map(value):
    value = value.strip()
    if not (value.startswith("{") and value.endswith("}")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return {}
    entries = [entry.strip() for entry in inner.split(",")]
    data = {}
    for entry in entries:
        if not entry or ":" not in entry:
            continue
        key, raw_value = entry.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        list_value = _parse_inline_list(raw_value)
        if list_value is not None:
            data[key] = list_value
        else:
            data[key] = _strip_quotes(raw_value)
    return data


def read_frontmatter(path):
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    if len(lines) < 3 or lines[0].strip() != "---":
        return None, "Missing YAML frontmatter start (---)."

    data = {}
    idx = 1
    while idx < len(lines):
        line = lines[idx].strip()
        if line == "---":
            return data, None
        if line and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            raw_value = value.strip()
            list_value = _parse_inline_list(raw_value)
            map_value = _parse_inline_map(raw_value)
            if map_value is not None:
                data[key] = map_value
            elif list_value is not None:
                data[key] = list_value
            else:
                data[key] = _strip_quotes(raw_value)
        idx += 1

    return None, "Missing YAML frontmatter end (---)."


def _has_reserved_words(text):
    lowered = text.lower()
    return any(word in lowered for word in RESERVED_WORDS)


def validate_skill(skill_path):
    errors = []
    skill_md = os.path.join(skill_path, "SKILL.md")
    if not os.path.isfile(skill_md):
        errors.append("SKILL.md not found.")
        return errors

    frontmatter, err = read_frontmatter(skill_md)
    if err:
        errors.append(err)
        return errors

    if frontmatter is None:
        errors.append("Frontmatter could not be parsed.")
        return errors

    skill_folder = os.path.basename(os.path.abspath(skill_path))
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    metadata = frontmatter.get("metadata")
    allowed_tools = frontmatter.get("allowed-tools")
    compatibility = frontmatter.get("compatibility")

    extra_keys = set(frontmatter.keys()) - ALLOWED_KEYS
    if extra_keys:
        errors.append(f"Unsupported frontmatter keys: {', '.join(sorted(extra_keys))}.")

    if not name:
        errors.append("Frontmatter missing name.")
    else:
        if not (1 <= len(name) <= 64):
            errors.append("Name must be 1-64 characters long.")
        if not KEBAB_RE.match(name):
            errors.append("Name must be kebab-case.")
        if name != skill_folder:
            errors.append("Skill name must match the folder name.")
        if _has_reserved_words(name):
            errors.append("Name must not include reserved words (claude, anthropic).")

    if not description:
        errors.append("Frontmatter missing description.")
    else:
        if not (1 <= len(description) <= 1024):
            errors.append("Description must be 1-1024 characters long.")
        if _has_reserved_words(description):
            errors.append("Description must not include reserved words (claude, anthropic).")
        if XML_TAG_RE.search(description):
            errors.append("Description must not include XML/HTML tags.")
        lowered = description.lower()
        if "use" not in lowered and "when" not in lowered:
            errors.append("Description should include usage trigger keywords (use/when).")

    if compatibility is not None and not isinstance(compatibility, str):
        errors.append("Compatibility must be a string if provided.")

    if allowed_tools is not None:
        if not isinstance(allowed_tools, list):
            errors.append("Allowed-tools must be a list when provided.")
        else:
            for tool in allowed_tools:
                if not isinstance(tool, str) or not KEBAB_RE.match(tool):
                    errors.append("Allowed-tools entries must be kebab-case strings.")
                    break

    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("Metadata must be a map if provided.")
        else:
            version = metadata.get("version")
            tags = metadata.get("tags")
            if version is not None and not (isinstance(version, str) and SEMVER_RE.match(version)):
                errors.append("Metadata version must be semantic (X.Y.Z).")
            if tags is not None:
                if not isinstance(tags, list):
                    errors.append("Metadata tags must be a list if provided.")
                else:
                    for tag in tags:
                        if not isinstance(tag, str) or not KEBAB_RE.match(tag):
                            errors.append("Metadata tags must be kebab-case strings.")
                            break

    with open(skill_md, "r", encoding="utf-8") as handle:
        line_count = len(handle.read().splitlines())
    if line_count > 500:
        errors.append("SKILL.md should be 500 lines or fewer.")

    return errors


def main():
    args = parse_args()
    skill_path = os.path.abspath(args.skill_path)
    errors = validate_skill(skill_path)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
