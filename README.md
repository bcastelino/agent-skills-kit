# agent-skills-kit

Toolkit for authoring and packaging Agent Skills. Includes a meta skill, templates, a sample skill, and scripts for validation and packaging.

## Repository Structure

```text
agent-skills-kit/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── skill-creator/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── basic.md
│   │       └── advanced.md
│   └── example-skill/
│       ├── SKILL.md
│       └── scripts/
│           └── README.md
├── scripts/
│   ├── init_skill.py
│   ├── validate_skill.py
│   └── package_skill.py
├── LICENSE
└── README.md
```

## Quickstart

1. Update owner metadata in .claude-plugin/marketplace.json.
2. Use skill-creator or run the toolkit scripts to create new skills.
3. Validate and package skills for distribution.

### Toolkit Scripts

```bash
python scripts/init_skill.py my-new-skill
python scripts/validate_skill.py skills/my-new-skill
python scripts/package_skill.py skills/my-new-skill
```

## IDE Setup

This kit works in Claude Code, VS Code, Cursor, and other IDEs. The skill files are plain Markdown with optional scripts.

### Claude Code

Add the marketplace:

```bash
/plugin marketplace add https://github.com/YourUsername/agent-skills-kit.git
```

Local development:

```bash
/plugin marketplace add ./agent-skills-kit
```

Then ask: "Use skill-creator to build a new skill for your task."

### VS Code

1. Open the repository folder.
2. Use the integrated terminal to run the toolkit scripts.
3. Edit skills in skills/{skill-name}/SKILL.md.

### Cursor

1. Open the repository folder.
2. Use the terminal to run toolkit scripts.
3. Use the templates to author new skills.

### Other IDEs

1. Clone the repository locally.
2. Run the toolkit scripts with Python.
3. Open and edit SKILL.md files directly.

## Creating a Skill

Use the skill-creator or start from templates:

- skills/skill-creator/templates/basic.md for instruction-only skills
- skills/skill-creator/templates/advanced.md for skills with scripts

After authoring:

```bash
python scripts/validate_skill.py skills/{skill-name}
python scripts/package_skill.py skills/{skill-name}
```

## Compatibility Notes

- Keep descriptions specific; they are the primary trigger for skill activation.
- Place large references in references/ to keep SKILL.md concise.
- Prefer scripts for deterministic tasks.
