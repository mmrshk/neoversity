import argparse
import shutil
import sys
from pathlib import Path


def _unique_destination(dest_file: Path) -> Path:
    if not dest_file.exists():
        return dest_file

    stem, suffix = dest_file.stem, dest_file.suffix
    n = 1

    while True:
        candidate = dest_file.with_name(f"{stem}_{n}{suffix}")
        if not candidate.exists():
            return candidate
        n += 1


def _extension_subdir_name(path: Path) -> str:
    return path.suffix.lower().lstrip(".") or "no_extension"


def _copy_file_into_extension_folder(src_file: Path, dest_root: Path) -> None:
    target_dir = dest_root / _extension_subdir_name(src_file)

    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Не вдалося створити {target_dir}: {e}", file=sys.stderr)
        return

    dest_file = _unique_destination(target_dir / src_file.name)

    try:
        shutil.copy2(src_file, dest_file)
    except (OSError, shutil.Error) as e:
        print(f"Не вдалося скопіювати {src_file} → {dest_file}: {e}", file=sys.stderr)


def copy_tree_by_extension(src_dir: Path, dest_root: Path) -> None:
    try:
        entries = list(src_dir.iterdir())
    except OSError as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}", file=sys.stderr)
        return

    for item in entries:
        try:
            if item.is_dir():
                copy_tree_by_extension(item, dest_root)
            elif item.is_file():
                _copy_file_into_extension_folder(item, dest_root)
        except OSError as e:
            print(f"Помилка при обробці {item}: {e}", file=sys.stderr)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли в теку призначення, сортуючи за розширенням.",
    )
    parser.add_argument("source", type=Path, help="Вихідна директорія")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Директорія призначення (за замовчуванням: dist)",
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()

    if not source.is_dir():
        print(f"Помилка: «{source}» не є директорією або недоступна.", file=sys.stderr)
        sys.exit(1)

    try:
        destination.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Не вдалося створити директорію призначення {destination}: {e}", file=sys.stderr)
        sys.exit(1)

    copy_tree_by_extension(source, destination)


if __name__ == "__main__":
    main()
