from common import (
    DISABLED_DIR,
    ENABLED_DIR,
    confirm,
    ensure_dirs,
    list_skill_dirs,
    print_numbered,
    prompt_selection,
)


def main():
    ensure_dirs()
    disabled = list_skill_dirs(DISABLED_DIR)

    if not disabled:
        print("No disabled skills to enable.")
        return

    print("Disabled skills:")
    print_numbered(disabled)
    idx = prompt_selection(len(disabled), "Select a skill to enable (or 'q' to quit): ")
    if idx is None:
        print("Aborted.")
        return

    selected = disabled[idx]
    dest = ENABLED_DIR / selected.name

    print(f"\nEnable '{selected.name}'? It will be moved to {ENABLED_DIR}.")
    if not confirm("Confirm [y/N]: "):
        print("Cancelled.")
        return

    if dest.exists():
        print(f"Destination already exists: {dest}")
        print("Aborting without changes.")
        return

    selected.rename(dest)
    print(f"Enabled: {selected.name}")
    print("Restart Codex to apply changes.")


if __name__ == "__main__":
    main()
