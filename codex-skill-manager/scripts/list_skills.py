from common import ENABLED_DIR, DISABLED_DIR, ensure_dirs, list_skill_dirs, print_numbered


def main():
    ensure_dirs()
    enabled = list_skill_dirs(ENABLED_DIR)
    disabled = list_skill_dirs(DISABLED_DIR)

    print("Enabled skills:")
    if enabled:
        print_numbered(enabled)
    else:
        print("(none)")

    print("\nDisabled skills:")
    if disabled:
        print_numbered(disabled)
    else:
        print("(none)")


if __name__ == "__main__":
    main()
