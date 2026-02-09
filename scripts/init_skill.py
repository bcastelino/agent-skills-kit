#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path C:/custom/location
"""

import argparse
import re
import sys
from pathlib import Path

KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64

SKILL_TEMPLATE = """---
name: {skill_name}
description: Use this when [TODO: describe when this skill applies and what it does].
license: MIT
metadata: {{version: "0.1.0", tags: [example]}}
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables.]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

1. Workflow-Based (best for sequential processes)
   - Use when there are clear step-by-step procedures.
   - Structure: Overview -> Workflow Decision Tree -> Steps

2. Task-Based (best for tool collections)
   - Use when the skill offers different operations.
   - Structure: Overview -> Quick Start -> Task Categories

3. Reference/Guidelines (best for standards or specifications)
   - Use for style guides, policies, or requirements.
   - Structure: Overview -> Guidelines -> Specifications -> Usage

4. Capabilities-Based (best for integrated systems)
   - Use when the skill provides multiple interrelated features.
   - Structure: Overview -> Core Capabilities -> Feature Details

Delete this section after choosing a structure.]

## Example Triggers

- [TODO: Add short example user request]
- [TODO: Add another example user request]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. Include concrete examples, decision trees, and references to scripts, assets, or references as needed.]

## Resources

This skill includes example resource directories that demonstrate how to organize bundled resources:

### scripts/
Executable code (Python/Bash/etc.) for deterministic operations.

### references/
Documentation intended to be loaded into context for detailed guidance.

### assets/
Files used in output (templates, images, fonts, boilerplate).

Any unneeded directories can be deleted.
"""

EXAMPLE_SCRIPT = """#!/usr/bin/env python3
'''Example helper script for {skill_name}.

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.
'''
"""


def main():
    parser = argparse.ArgumentParser(description="Initialize a new skill directory.")
    parser.add_argument("skill_name", help="Skill name in kebab-case")
    parser.add_argument("--path", required=True, help="Output directory path")
    args = parser.parse_args()

    skill_name = args.skill_name.strip()
    if not KEBAB_RE.match(skill_name):
        print("Error: skill name must be kebab-case.")
        return 1
    if len(skill_name) > MAX_NAME_LENGTH:
        print("Error: skill name must be 64 characters or fewer.")
        return 1

    skill_dir = Path(args.path).resolve() / skill_name
    print(f"Initializing skill: {skill_name}")
    print(f"Location: {skill_dir}")
    print()

    if skill_dir.exists():
        print(f"Error: skill directory already exists: {skill_dir}")
        return 1

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
    except Exception as exc:
        print(f"Error creating directory: {exc}")
        return 1

    skill_title = " ".join(word.capitalize() for word in skill_name.split("-"))
    skill_md_path = skill_dir / "SKILL.md"
    try:
        skill_md_path.write_text(SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title), encoding="utf-8")
        print("Created SKILL.md")
    except Exception as exc:
        print(f"Error creating SKILL.md: {exc}")
        return 1

    try:
        scripts_dir = skill_dir / "scripts"
        references_dir = skill_dir / "references"
        assets_dir = skill_dir / "assets"
        scripts_dir.mkdir(exist_ok=True)
        references_dir.mkdir(exist_ok=True)
        assets_dir.mkdir(exist_ok=True)

        example_script = scripts_dir / "example.py"
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name), encoding="utf-8")

        example_reference = references_dir / "api_reference.md"
        example_reference.write_text("# Reference Documentation\n\nReplace with real reference content.\n", encoding="utf-8")

        example_asset = assets_dir / "example_asset.txt"
        example_asset.write_text("Placeholder asset. Replace with real assets or delete.\n", encoding="utf-8")
        print("Created scripts/, references/, and assets/ with example files")
    except Exception as exc:
        print(f"Error creating resource directories: {exc}")
        return 1

    print()
    print(f"Skill '{skill_name}' initialized successfully.")
    print("Next steps:")
    print("1. Edit SKILL.md and complete TODO items")
    print("2. Customize or delete example files in scripts/, references/, and assets/")
    print("3. Run the validator when ready")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
