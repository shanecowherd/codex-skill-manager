# Codex Skill Manager

A Codex skill that helps you list, disable, and enable other Codex skills by moving them
between the enabled skills folder and a disabled folder.

## Install

### From GitHub (recommended)

Use the skill installer from your Codex home:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path codex-skill-manager
```

This installs into `~/.codex/skills/codex-skill-manager`.

### From a local clone

```bash
cp -R codex-skill-manager ~/.codex/skills/
```

## Usage

Ask Codex to use the `codex-skill-manager` skill and follow its prompts.

Notes:
- Disabled skills live in `~/.codex/skills.disabled` by default.
- You may need to restart Codex after enabling or disabling skills.
