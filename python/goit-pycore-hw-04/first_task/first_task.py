from pathlib import Path


current_dir = Path(__file__).parent


def total_salary(path):
    try:
        file_path = current_dir / path
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = [line.strip().split(',') for line in file.readlines()]
            salaries = []

            for row in file_data:
                if len(row) >= 2:
                  try:
                    salaries.append(int(row[1]))
                  except ValueError:
                    pass

            salaries = [int(row[1]) for row in file_data]

            if not salaries:
              return 0,0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    except FileNotFoundError:
      return 'File not found'


if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
