import sys
from pathlib import Path
from colorama import Fore, Style


def sort_by_name(item):
    return item.name.lower()


def print_tree(path, prefix=""):
    dirs = sorted([p for p in path.iterdir() if p.is_dir()], key=sort_by_name)
    files = sorted([p for p in path.iterdir() if p.is_file()], key=sort_by_name)
    items = dirs + files

    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        connector = "┗ " if is_last_item else "┣ "

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            extension = "   " if is_last_item else "┃ "
            print_tree(item, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: вкажіть шлях до директорії")
        print(f"Використання: python third_task.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує - {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: вказаний шлях не є директорією - {dir_path}")
        sys.exit(1)

    print(f"{Fore.YELLOW}📦 {dir_path.name}{Style.RESET_ALL}")
    print_tree(dir_path)