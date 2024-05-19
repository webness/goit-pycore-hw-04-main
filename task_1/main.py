from pathlib import Path
from typing import Tuple

def total_salary(file_path: str) -> Tuple[float, float]:
    total, average = 0.0, 0.0
    absolute_path = Path(file_path).resolve()

    print("Calculating total and average salary from file:", absolute_path)

    try:
        with open(absolute_path, "r", encoding="utf-8") as file:
            records = file.readlines()
            if not records:
                raise ValueError("The file is empty.")
            for record in records:
                _, salary = record.split(",")
                total += float(salary.strip())

        average = total / len(records)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {absolute_path} does not exist.")
    except ValueError as e:
        raise ValueError(f"Error processing file: {e}")

    return total, average

def main():
    file_path = input("Enter the salaries file path: ")

    try:
        total, average = total_salary(file_path)
        print(f"Total salary: {total:.2f}, Average salary: {average:.2f}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
