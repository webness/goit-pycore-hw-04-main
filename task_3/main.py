from pathlib import Path
import sys
import colorama

def display_directory_tree(directory_path: str | Path, level: int = 0) -> None:
    colorama.init()

    path = Path(directory_path)

    if not path.exists():
        raise ValueError(f"Path not found: {path}")

    if path.is_file():
        raise ValueError("Path must be a directory.")

    print(f"{'  ' * level}{colorama.Fore.LIGHTBLUE_EX}{path.name}/{colorama.Style.RESET_ALL}")

    subdirs = sorted([item for item in path.iterdir() if item.is_dir()])
    files = sorted([item for item in path.iterdir() if item.is_file()])

    for subdir in subdirs:
        display_directory_tree(subdir, level + 1)

    for file in files:
        print(f"{'  ' * (level + 1)}{colorama.Fore.LIGHTYELLOW_EX}{file.name}{colorama.Style.RESET_ALL}")

    colorama.deinit()

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    try:
        display_directory_tree(sys.argv[1])
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
