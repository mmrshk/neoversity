import random
import timeit

from statistics import median
from task3 import insertion_sort, merge_sort, tim_sort


def _make_data(n, kind):
    rng = random.Random(42)

    if kind == "random":
      return [rng.randint(-10000, 10000) for _ in range(n)]
    if kind == "sorted":
      return list(range(n))
    if kind == "reversed":
      return list(range(n, 0, -1))
    if kind == "nearly_sorted":
        a = list(range(n))

        for _ in range(max(1, n // 50)):
          i, j = rng.randrange(n), rng.randrange(n)
          a[i], a[j] = a[j], a[i]

        return a

    raise ValueError(kind)

if __name__ == "__main__":
    sizes_kinds = [
        (500, "random"),
        (2000, "random"),
        (5000, "random"),
        (5000, "sorted"),
        (5000, "reversed"),
        (5000, "nearly_sorted"),
    ]
    algorithms = [
        ("insertion_sort", "insertion_sort(data[:])"),
        ("merge_sort", "merge_sort(data[:])"),
        ("tim_sort (наш)", "tim_sort(data[:])"),
        ("sorted() вбудований", "sorted(data)"),
    ]
    print("Час одного сортування (сек), min з 5 повторів timeit.repeat\n")
    header = f"{'n':>6} {'тип даних':<16}"
    for label, _ in algorithms:
        header += f"{label:>20}"

    print(header)
    print("-" * len(header))

    for n, kind in sizes_kinds:
        data = _make_data(n, kind)

        g = {
            "data": data,
            "insertion_sort": insertion_sort,
            "merge_sort": merge_sort,
            "tim_sort": tim_sort,
        }

        row = f"{n:>6} {kind:<16}"

        for _, stmt in algorithms:
            t = min(timeit.repeat(stmt, globals=g, repeat=5, number=1))
            row += f"{t:>20.6f}"
        print(row)

    print(
        "\ninsertion_sort і tim_sort змінюють список — у вимірюванні використовується data[:]. "
        "Для дуже великих n зменш n у таблиці або збільш number у timeit, якщо час занадто малий."
    )
