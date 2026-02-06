---
name: skill-creator
description: Interactive assistant that scaffolds new Agent Skills. Use this when the user wants to create, write, or generate a new skill.
license: MIT
metadata: {version: "1.0.0", tags: [skill-authoring, scaffolding, templates]}
---

# Skill Creator

## Purpose
Create a valid skill directory structure and produce a high-quality SKILL.md using the repository templates and rules.

## When to Use
- The user asks to create a new skill
- The user wants to update or refactor an existing skill
- The user needs a valid skill package for an IDE or agent runtime

## Process
1. Interview to understand the task, goals, inputs, outputs, and constraints.
2. Decide whether the skill needs only instructions (Markdown) or also scripts, references, or assets.
3. Scaffold the skill folder at skills/<user-skill-name>/.
4. Generate SKILL.md with valid frontmatter and concise instructions.
5. Add scripts/, references/, and assets/ only if needed.
6. Validate the skill and update any placeholders.

## Validation Rules
- Name must be kebab-case (example: git-helper).
- Frontmatter must be valid YAML wrapped in --- lines.
- Required fields: name, description.
- Description must be specific and include trigger keywords.
- If version is present, use semantic versioning (X.Y.Z).

## Template Usage
- Use templates/basic.md for instruction-only skills.
- Use templates/advanced.md for skills that require scripts.
- Customize placeholders and remove unused sections.

## Best Practices
- Progressive disclosure: only the description is always in context. Make it precise.
- Context efficiency: keep SKILL.md short; move details to references/.
- Determinism: if accuracy must be exact, include scripts and document how to run them.
- Avoid duplication: do not repeat large reference content in SKILL.md.

## Toolkit Scripts (Optional)
If this repository includes toolkit scripts at scripts/:
- Run scripts/init_skill.py to scaffold a skill quickly.
- Run scripts/validate_skill.py to check structure and frontmatter.
- Run scripts/package_skill.py to build a zip for distribution.
