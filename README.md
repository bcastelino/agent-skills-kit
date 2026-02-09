<h1 align="center">Agent Skills Kit</h1>

> Toolkit for authoring and packaging Agent Skills. Includes a meta skill, templates, a sample skill, and scripts for validation and packaging.

![Agent Skills Architecture](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg&w=3840&q=75)

## Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```markdown
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

## Quickstart

1. Update owner metadata in .claude-plugin/marketplace.json.
2. Use skill-creator or run the toolkit scripts to create new skills.
3. Validate and package skills for distribution.

### Toolkit Scripts

Toolkit scripts for creating and packaging skills.

- init_skill.py: scaffold a new skill directory

```bash
python scripts/init_skill.py my-new-skill
```

- validate_skill.py: validate SKILL.md frontmatter and structure

```bash
python scripts/validate_skill.py skills/my-new-skill
```

- package_skill.py: validate and zip a skill for distribution

```bash
python scripts/package_skill.py skills/my-new-skill
```

The initializer creates example files in scripts/, references/, and assets/ so you can customize or delete them.

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
- Include usage triggers in the description ("Use this when ...").
- Place large references in references/ to keep SKILL.md concise.
- Prefer scripts for deterministic tasks.

## Validation Rules

The validator enforces Agent Skills best practices and the open spec:

- Name must be kebab-case, 1-80 characters, and match the folder name
- Description must be 1-1024 characters and include trigger keywords
- Avoid reserved words in name/description (claude, anthropic)
- No XML/HTML tags in the description
- SKILL.md should be 500 lines or fewer

## References

- Agent Skills best practices: [platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic skills repo: [github.com/anthropics/skills](https://github.com/anthropics/skills)
- Skill creator reference: [github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Open spec: [agentskills.io/home](https://agentskills.io/home)

## Author

<table>
   <tr>
      <td>
         <div style="flex-shrink: 0; order: 2;">
            <img src="https://raw.githubusercontent.com/bcastelino/brian-portfolio/refs/heads/main/public/personal/profile.jpg" alt="Brian Denis Castelino" style="border-radius: 50%; width: 180px; height: 180px; object-fit: cover; border: 4px solid #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
         </div>
      </td>
      <td>
         <div align="left" style="padding: 20px;">
            <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; width: 100%; max-width: 800px; gap: 40px; text-align: center;">
               <div style="flex: 1; min-width: 250px; order: 1;">
                  <h1 style="font-size: 2em; margin-bottom: 5px; color: #333;">Brian Denis Castelino</h1>
                  <p style="font-size: 1.2em; color: #555; margin-bottom: 10px;">Data Analytics Engineer | AI Enthusiast</p>
                  <p style="font-size: 1em; color: #777; margin-bottom: 20px;">I turn vague ideas into clean, working systems, because someone’s got to 🤖</p>
                  <div style="display: flex; justify-content: center; gap: 30px;">
                     <a href="https://github.com/bcastelino" target="_blank" style="text-decoration: none;">
                     <img src="https://cdn-icons-png.flaticon.com/512/4494/4494756.png" alt="GitHub" width="30" height="30" style="width: 30px; height: 30px;">
                     </a>
                   &nbsp; &nbsp; &nbsp;
                     <a href="https://linkedin.com/in/cas7elino" target="_blank" style="text-decoration: none;">
                     <img src="https://cdn-icons-png.flaticon.com/512/4494/4494498.png" alt="LinkedIn" width="30" height="30" style="width: 30px; height: 30px;">
                     </a>
                   &nbsp; &nbsp; &nbsp;
                     <a href="https://twitter.com/cas7elino" target="_blank" style="text-decoration: none;">
                     <img src="https://cdn-icons-png.flaticon.com/512/4494/4494481.png" alt="Twitter" width="30" height="30" style="width: 30px; height: 30px;">
                     </a>
                   &nbsp; &nbsp; &nbsp;
                     <a href="https://instagram.com/cas7elino" target="_blank" style="text-decoration: none;">
                     <img src="https://cdn-icons-png.flaticon.com/512/4494/4494489.png" alt="Instagram" width="30" height="30" style="width: 30px; height: 30px;">
                     </a>
                   &nbsp; &nbsp; &nbsp;
                     <a href="https://brianc.framer.website/" target="_blank" style="text-decoration: none;">
                     <img src="https://cdn-icons-png.flaticon.com/512/4494/4494636.png" alt="Website" width="30" height="30" style="width: 30px; height: 30px;">
                     </a>
                  </div>
               </div>
      </td>
      </div>
      </div>
   </tr>
</table>