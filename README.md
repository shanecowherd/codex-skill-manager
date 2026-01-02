# Codex Skill Manager

A Codex skill that helps you list, disable, and enable other Codex skills by moving them
between the enabled skills folder and a disabled folder.

## Install (Codex)

### With Codex (recommended)

In Codex, use the `skill-installer` and provide this URL:

```
https://github.com/shanecowherd/codex-skill-manager/tree/main/codex-skill-manager
```

Codex will install into `~/.codex/skills/codex-skill-manager`. Restart Codex after installation.

### Manual install (Codex)

```bash
cp -R codex-skill-manager ~/.codex/skills/
```

Restart Codex after manual installation.

## Usage

Ask Codex to use the `codex-skill-manager` skill and follow its prompts.

Notes:
- Disabled skills live in `~/.codex/skills.disabled` by default.
- You may need to restart Codex after enabling or disabling skills.
