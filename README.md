<div align="center">

  <h1>Agent Skills Kit</h1>

  <img src="assets/images/agent-skills-banner.png" alt="Agent Skills Kit Banner" width="100%" />

  <p>
    <b>Write Once, Run Anywhere.</b><br>
    The universal standard for building, validating, and packaging AI Agent Skills.
  </p>

  <p>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Platform-VS%20Code%20%7C%20Cursor%20%7C%20Claude%20%7C%20Antigravity-blueviolet" alt="Supported Platforms">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
    </a>
  </p>
</div>

---
> Toolkit for authoring and packaging Agent Skills. Includes a meta skill, templates, a sample skill, and scripts for validation and packaging.

---
## Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```markdown
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

---
## Quickstart

1. Update owner metadata in .claude-plugin/marketplace.json.
2. Use skill-creator or run the toolkit scripts to create new skills.
3. Validate and package skills for distribution.

### Toolkit Scripts

| Script | Purpose | Command |
|---|---|---|
| `scripts/init_skill.py` | Scaffold a new skill directory with starter resources | `python scripts/init_skill.py my-new-skill --path skills` |
| `scripts/validate_skill.py` | Validate `SKILL.md` frontmatter and structure | `python scripts/validate_skill.py skills/my-new-skill` |
| `scripts/package_skill.py` | Validate and package a skill as a zip archive | `python scripts/package_skill.py skills/my-new-skill` |

The initializer creates example files in `scripts/`, `references/`, and `assets/` so you can customize or delete them.

---
## Skills Catalog

| Category | Skills |
|---|---|
| Core Engineering & Quality | [skill-creator](skills/skill-creator) \| [software-architecture](skills/software-architecture) \| [clean-code](skills/clean-code) \| [code-reviewer](skills/code-reviewer) \| [code-review-excellence](skills/code-review-excellence) \| [requesting-code-review](skills/requesting-code-review) \| [commit](skills/commit) \| [context-optimization](skills/context-optimization) \| [vibe-code-auditor](skills/vibe-code-auditor) \| [code-refactoring-context-restore](skills/code-refactoring-context-restore) \| [code-refactoring-refactor-clean](skills/code-refactoring-refactor-clean) \| [code-refactoring-tech-debt](skills/code-refactoring-tech-debt) |
| AI, Agents & RAG | [ai-agent-development](skills/ai-agent-development) \| [ai-agents-architect](skills/ai-agents-architect) \| [ai-engineer](skills/ai-engineer) \| [ai-ml](skills/ai-ml) \| [ai-product](skills/ai-product) \| [crewai](skills/crewai) \| [langgraph](skills/langgraph) \| [mcp-builder](skills/mcp-builder) \| [embedding-strategies](skills/embedding-strategies) \| [rag-engineer](skills/rag-engineer) \| [rag-implementation](skills/rag-implementation) \| [notebooklm](skills/notebooklm) |
| Data Engineering & Analytics | [business-analyst](skills/business-analyst) \| [data-engineer](skills/data-engineer) \| [data-scientist](skills/data-scientist) \| [data-storytelling](skills/data-storytelling) \| [data-engineering-data-driven-feature](skills/data-engineering-data-driven-feature) \| [data-engineering-data-pipeline](skills/data-engineering-data-pipeline) \| [spark-optimization](skills/spark-optimization) \| [ml-pipeline-workflow](skills/ml-pipeline-workflow) |
| ML, MLOps & Training | [ml-engineer](skills/ml-engineer) \| [mlops-engineer](skills/mlops-engineer) \| [temporal-python-pro](skills/temporal-python-pro) \| [python-pro](skills/python-pro) \| [python-testing-patterns](skills/python-testing-patterns) \| [unit-testing-test-generate](skills/unit-testing-test-generate) |
| Python & API Development | [python-development-python-scaffold](skills/python-development-python-scaffold) \| [python-fastapi-development](skills/python-fastapi-development) \| [fastapi-pro](skills/fastapi-pro) \| [fastapi-router-py](skills/fastapi-router-py) \| [fastapi-templates](skills/fastapi-templates) \| [uv-package-manager](skills/uv-package-manager) |
| Databases & SQL | [database-design](skills/database-design) \| [database-migration](skills/database-migration) \| [database-optimizer](skills/database-optimizer) \| [database-cloud-optimization-cost-optimize](skills/database-cloud-optimization-cost-optimize) \| [nosql-expert](skills/nosql-expert) \| [postgresql](skills/postgresql) \| [postgres-best-practices](skills/postgres-best-practices) \| [sql-pro](skills/sql-pro) \| [sql-optimization-patterns](skills/sql-optimization-patterns) |
| Cloud, DevOps & GitHub | [aws-skills](skills/aws-skills) \| [cloud-architect](skills/cloud-architect) \| [cloud-devops](skills/cloud-devops) \| [gcp-cloud-run](skills/gcp-cloud-run) \| [prometheus-configuration](skills/prometheus-configuration) \| [git-advanced-workflows](skills/git-advanced-workflows) \| [github-actions-templates](skills/github-actions-templates) \| [github-automation](skills/github-automation) \| [github-workflow-automation](skills/github-workflow-automation) |
| Product, Automation & Domain Tools | [full-stack-orchestration-full-stack-feature](skills/full-stack-orchestration-full-stack-feature) \| [game-development](skills/game-development) \| [computer-vision-expert](skills/computer-vision-expert) \| [scientific-skills](skills/scientific-skills) \| [vulnerability-scanner](skills/vulnerability-scanner) \| [code-documentation-code-explain](skills/code-documentation-code-explain) \| [code-documentation-doc-generate](skills/code-documentation-doc-generate) \| [pdf-official](skills/pdf-official) \| [pptx-official](skills/pptx-official) \| [youtube-summarizer](skills/youtube-summarizer) \| [hugging-face-cli](skills/hugging-face-cli) \| [hugging-face-jobs](skills/hugging-face-jobs) \| [tailored-resume-generator](skills/tailored-resume-generator) \| [video-downloader](skills/video-downloader) |

---
## IDE Compatibility & Setup

This kit works in VS Code, Cursor, Antigravity, Claude CLI/Web, and other IDEs because skills are plain Markdown folders.

### Compatibility Summary

| IDE / Platform | Default Skill Location | Quick Setup | Docs |
|---|---|---|---|
| VS Code (GitHub Copilot) | `.github/skills` | Set `chat.agentSkillsLocations` to include `./skills`, or symlink `skills` → `.github/skills` | https://code.visualstudio.com/docs/copilot/customization/agent-skills |
| Cursor | `.cursor/skills` or `.claude/skills` | Symlink `skills` → `.cursor/skills`, or import as remote GitHub rule | https://cursor.com/docs/context/skills |
| Google Antigravity | `.agent/skills` | Create `.agent/skills` and link/copy the repository `skills/` folder | https://antigravity.google/docs/skills |
| Claude (CLI & Web) | `.claude/skills` (project or global) | Add plugin source with `/plugin marketplace add ...` or manually copy skill folders | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |

### Quick Setup Commands

| Platform | macOS / Linux | Windows |
|---|---|---|
| Cursor | `ln -s skills .cursor/skills` | `mklink /D .cursor\skills skills` |
| Antigravity | `mkdir -p .agent && ln -s ../skills .agent/skills` | `mkdir .agent` + `mklink /D .agent\skills ..\skills` |

For Claude CLI plugin registration:

```bash
/plugin marketplace add https://github.com/bcastelino/agent-skills-kit.git
```

---
## Creating a Skill

<img src="assets/images/ai-skill-factory.png" alt="Agent Skills Kit Banner" width="100%" />

Use the skill-creator or start from templates:

- `skills/skill-creator/templates/basic.md` for instruction-only skills
- `skills/skill-creator/templates/advanced.md` for skills with scripts

After authoring:

```bash
python scripts/validate_skill.py skills/{skill-name}
python scripts/package_skill.py skills/{skill-name}
```

---
## Compatibility Notes

- Keep descriptions specific; they are the primary trigger for skill activation.
- Include usage triggers in the description ("Use this when ...").
- Place large references in references/ to keep SKILL.md concise.
- Prefer scripts for deterministic tasks.

---
## Validation Rules

The validator enforces Agent Skills best practices and the open spec:

- Name must be kebab-case, 1-64 characters, and match the folder name
- Description must be 1-1024 characters and include trigger keywords (use/when)
- Avoid reserved words in name/description (claude, anthropic)
- No XML/HTML tags in the description
- Frontmatter supports flat key/value pairs with inline lists/maps only; nested YAML and multi-line values are not supported
- Allowed frontmatter keys: name, description, license, compatibility, allowed-tools, metadata
- SKILL.md should be 500 lines or fewer

---
## References

- Agent Skills best practices: [platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic skills repo: [github.com/anthropics/skills](https://github.com/anthropics/skills)
- Skill creator reference: [github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Awesome Claude Skills: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- Open spec: [agentskills.io/home](https://agentskills.io/home)

---
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
