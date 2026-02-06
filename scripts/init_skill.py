#!/usr/bin/env python3
import argparse
import os
import re
import sys

KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args():
    parser = argparse.ArgumentParser(description="Initialize a new skill directory.")
    parser.add_argument("skill_name", help="Skill name in kebab-case")
    parser.add_argument("--path", default=".", help="Output directory path")
    return parser.parse_args()


def ensure_kebab(name):
    return KEBAB_RE.match(name) is not None


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    args = parse_args()
    skill_name = args.skill_name.strip()

    if not ensure_kebab(skill_name):
        print("Error: skill name must be kebab-case.")
        return 1

    target_root = os.path.abspath(args.path)
    skill_root = os.path.join(target_root, "skills", skill_name)

    if os.path.exists(skill_root) and os.listdir(skill_root):
        print("Error: target skill directory already exists and is not empty.")
        return 1

    os.makedirs(skill_root, exist_ok=True)

    skill_md = os.path.join(skill_root, "SKILL.md")
    template = (
        "---\n"
        f"name: {skill_name}\n"
        "description: <one sentence that triggers this skill>\n"
        "version: 0.1.0\n"
        "tags: [example]\n"
        "license: MIT\n"
        "---\n\n"
        f"# {skill_name}\n\n"
        "## Purpose\n"
        "<what this skill does>\n\n"
        "## When to Use\n"
        "<clear trigger conditions>\n\n"
        "## Steps\n"
        "1. <step one>\n"
        "2. <step two>\n"
    )
    write_file(skill_md, template)

    for folder, note in [
        ("scripts", "Executable code for deterministic steps."),
        ("references", "Documentation or domain knowledge."),
        ("assets", "Templates or files used in outputs."),
    ]:
        subdir = os.path.join(skill_root, folder)
        os.makedirs(subdir, exist_ok=True)
        write_file(os.path.join(subdir, "README.md"), note + "\n")

    print(f"Initialized skill at {skill_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
