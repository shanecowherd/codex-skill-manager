---
name: codex-skill-manager
description: Manage Codex skills by listing installed skills, disabling a selected skill by moving it to a disabled folder, and re-enabling by moving it back. Use when the user asks to enable/disable skills, list enabled/disabled skills, or manage skill locations.
---

# Codex Skill Manager

## Overview

List installed skills, disable a skill by moving it to `~/.codex/skills.disabled`, and enable a disabled skill by moving it back to `~/.codex/skills`.

## Quick start

Use the scripts in `scripts/` for deterministic results:

- `scripts/list_skills.py` to list enabled and disabled skills
- `scripts/disable_skill.py` to disable a selected skill
- `scripts/enable_skill.py` to enable a selected skill

## Workflow

### 1) List skills

Run:

```bash
python3 scripts/list_skills.py
```

This prints two numbered lists: enabled skills and disabled skills.

### 2) Disable a skill

Run:

```bash
python3 scripts/disable_skill.py
```

The script:
- Lists enabled skills
- Prompts for a selection number
- Asks for confirmation
- Moves the selected folder from `~/.codex/skills` to `~/.codex/skills.disabled`

### 3) Enable a skill

Run:

```bash
python3 scripts/enable_skill.py
```

The script:
- Lists disabled skills
- Prompts for a selection number
- Asks for confirmation
- Moves the selected folder from `~/.codex/skills.disabled` to `~/.codex/skills`

## Notes

- Keep the `.system` skill folder enabled.
- If a destination already exists, the script aborts without overwriting.
- You may need to restart Codex after enabling or disabling skills.
