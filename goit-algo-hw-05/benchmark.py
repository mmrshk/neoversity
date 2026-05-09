from timeit import Timer
from pathlib import Path

from boyer_moore import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search

current_dir = Path(__file__).parent


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def measure(func, text, pattern, repeat=5, number=10):
    timer = Timer(lambda: func(text, pattern))
    times = timer.repeat(repeat=repeat, number=number)

    return min(times) / number


if __name__ == "__main__":
    article1 = read_file(current_dir / "стаття 1.txt")
    article2 = read_file(current_dir / "стаття 2.txt")

    # Підрядки, що дійсно існують у відповідних текстах
    existing_pattern_1 = "алгоритм"
    existing_pattern_2 = "рекомендаційної системи"

    # Вигаданий підрядок, якого свідомо немає в жодному з текстів
    fake_pattern = "чому взагалі робити багато викликів за одну серію?"

    texts = [
        ("Стаття 1", article1, existing_pattern_1),
        ("Стаття 2", article2, existing_pattern_2),
    ]

    algorithms = [
        ("Boyer-Moore", boyer_moore_search),
        ("KMP",         kmp_search),
        ("Rabin-Karp",  rabin_karp_search),
    ]

    header = (
        f"{'Текст':<10} {'Підрядок':<35} "
        f"{'Boyer-Moore (с)':>18} {'KMP (с)':>14} {'Rabin-Karp (с)':>18} {'Найшвидший':>14}"
    )
    print(header)
    print("-" * len(header))

    overall_totals = {name: 0.0 for name, _ in algorithms}
    per_text_totals = {}

    for text_name, text, existing in texts:
        per_text_totals[text_name] = {name: 0.0 for name, _ in algorithms}
        cases = [
            (f"існуючий: {existing!r}", existing),
            (f"вигаданий: {fake_pattern!r}", fake_pattern),
        ]

        for case_label, pattern in cases:
            results = {}
            for alg_name, alg in algorithms:
                t = measure(alg, text, pattern)
                results[alg_name] = t
                overall_totals[alg_name] += t
                per_text_totals[text_name][alg_name] += t

            fastest = min(results, key=results.get)
            print(
                f"{text_name:<10} {case_label:<35} "
                f"{results['Boyer-Moore']:>18.6f} {results['KMP']:>14.6f} "
                f"{results['Rabin-Karp']:>18.6f} {fastest:>14}"
            )

    print()
    print("Сумарний час за кожним текстом (існуючий + вигаданий підрядок):")
    print(f"{'Текст':<10} {'Boyer-Moore (с)':>18} {'KMP (с)':>14} {'Rabin-Karp (с)':>18} {'Найшвидший':>14}")
    print("-" * 76)
    for text_name, totals in per_text_totals.items():
        fastest = min(totals, key=totals.get)
        print(
            f"{text_name:<10} {totals['Boyer-Moore']:>18.6f} {totals['KMP']:>14.6f} "
            f"{totals['Rabin-Karp']:>18.6f} {fastest:>14}"
        )

    print()
    print("Загалом по обох текстах:")
    fastest_overall = min(overall_totals, key=overall_totals.get)
    for alg_name, total in overall_totals.items():
        marker = "  <-- найшвидший" if alg_name == fastest_overall else ""
        print(f"  {alg_name:<12}: {total:.6f} с{marker}")
