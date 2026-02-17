from pathlib import Path


current_dir = Path(__file__).parent


CAT_KEYS = ["id", "name", "age"]


def get_cats_info(path):
    try:
        file_path = current_dir / path

        with open(file_path, "r", encoding="utf-8") as file:
            file_data = [line.strip().split(",") for line in file if line.strip()]

            cats_info = [dict(zip(CAT_KEYS, cat_info)) for cat_info in file_data]
            return cats_info

    except FileNotFoundError:
        return "File not found"


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
