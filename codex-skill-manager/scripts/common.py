import os
from pathlib import Path

CODEX_HOME = Path(os.path.expanduser("~/.codex"))
ENABLED_DIR = CODEX_HOME / "skills"
DISABLED_DIR = CODEX_HOME / "skills.disabled"


def ensure_dirs():
    ENABLED_DIR.mkdir(parents=True, exist_ok=True)
    DISABLED_DIR.mkdir(parents=True, exist_ok=True)


def list_skill_dirs(root: Path):
    if not root.exists():
        return []
    return sorted(
        [p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")],
        key=lambda p: p.name.lower(),
    )


def print_numbered(skills):
    for idx, path in enumerate(skills, start=1):
        print(f"{idx}. {path.name}")


def prompt_selection(count, prompt):
    if count == 0:
        return None
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            return None
        if raw.isdigit():
            num = int(raw)
            if 1 <= num <= count:
                return num - 1
        print("Invalid selection. Enter a number or 'q' to quit.")


def confirm(prompt):
    raw = input(prompt).strip().lower()
    return raw in {"y", "yes"}
