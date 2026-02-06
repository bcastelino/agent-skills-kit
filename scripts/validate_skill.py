#!/usr/bin/env python3
import argparse
import os
import re
import sys

KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def parse_args():
    parser = argparse.ArgumentParser(description="Validate a skill directory.")
    parser.add_argument("skill_path", help="Path to a skill folder")
    return parser.parse_args()


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
            data[key.strip()] = value.strip()
        idx += 1

    return None, "Missing YAML frontmatter end (---)."


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

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    metadata = frontmatter.get("metadata", "")

    if not name:
        errors.append("Frontmatter missing name.")
    elif not KEBAB_RE.match(name):
        errors.append("Name must be kebab-case.")

    if not description or len(description) < 20:
        errors.append("Description must be specific (20+ characters).")

    if metadata:
        match = re.search(r"version\s*:\s*([0-9]+\.[0-9]+\.[0-9]+)", metadata)
        if match is None:
            errors.append("Metadata version must be semantic (X.Y.Z).")

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
