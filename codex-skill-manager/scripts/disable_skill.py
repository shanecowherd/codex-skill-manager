from pathlib import Path

from common import (
    DISABLED_DIR,
    ENABLED_DIR,
    confirm,
    ensure_dirs,
    list_skill_dirs,
    print_numbered,
    prompt_selection,
)


SYSTEM_DIR = ENABLED_DIR / ".system"


def main():
    ensure_dirs()
    enabled = list_skill_dirs(ENABLED_DIR)
    enabled = [p for p in enabled if p != SYSTEM_DIR]

    if not enabled:
        print("No enabled skills to disable.")
        return

    print("Enabled skills:")
    print_numbered(enabled)
    idx = prompt_selection(len(enabled), "Select a skill to disable (or 'q' to quit): ")
    if idx is None:
        print("Aborted.")
        return

    selected = enabled[idx]
    dest = DISABLED_DIR / selected.name

    print(f"\nDisable '{selected.name}'? It will be moved to {DISABLED_DIR}.")
    if not confirm("Confirm [y/N]: "):
        print("Cancelled.")
        return

    if dest.exists():
        print(f"Destination already exists: {dest}")
        print("Aborting without changes.")
        return

    selected.rename(dest)
    print(f"Disabled: {selected.name}")
    print("Restart Codex to apply changes.")


if __name__ == "__main__":
    main()
