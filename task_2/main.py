from pathlib import Path
from typing import List, Dict

def get_cats_info(file_path: str) -> List[Dict[str, any]]:
    cats = []
    absolute_path = Path(file_path).resolve()

    with open(absolute_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            try:
                cat_id, name, age = line.strip().split(",")
                cats.append({"id": cat_id, "name": name, "age": int(age)})
            except ValueError as e:
                print(f"Skipping invalid line: {line.strip()} ({e})")

    return cats

def main():
    base_path = Path(__file__).resolve().parent

    try:
        cats_info = get_cats_info(Path(base_path, "cats.txt"))
        print(cats_info)
    except FileNotFoundError as e:
        print(f"Error: File not found ({e})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
