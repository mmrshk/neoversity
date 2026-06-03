# Завдання 7. Використання методу Монте-Карло

# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків,
# обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів.
# Для кожного кидка визначте суму чисел, які випали на обох кубиках.
# Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції.
# Використовуючи ці дані, обчисліть імовірність кожної суми.

# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

# Сума	Імовірність
# 2	2.78% (1/36)
# 3	5.56% (2/36)
# 4	8.33% (3/36)
# 5	11.11% (4/36)
# 6	13.89% (5/36)
# 7	16.67% (6/36)
# 8	13.89% (5/36)
# 9	11.11% (4/36)
# 10	8.33% (3/36)
# 11	5.56% (2/36)
# 12	2.78% (1/36)

# Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

import random
from collections import Counter

import matplotlib.pyplot as plt

ANALYTICAL = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

def roll_two_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls: int = 1_000_000) -> dict[int, float]:
    counts = Counter(roll_two_dice() for _ in range(num_rolls))

    return {s: counts[s] / num_rolls for s in range(2, 13)}

def print_comparison(mc: dict[int, float]) -> None:
    print(f"{'Сума':<6} {'MC %':>10} {'Теор %':>10} {'Різниця':>10}")
    print("-" * 40)

    for s in range(2, 13):
        mc_pct = mc[s] * 100
        th_pct = ANALYTICAL[s] * 100
        diff = mc_pct - th_pct
        print(f"{s:<6} {mc_pct:>9.2f}% {th_pct:>9.2f}% {diff:>+9.2f}%")


def plot_probabilities(mc: dict[int, float]) -> None:
    sums = list(range(2, 13))
    mc_probs = [mc[s] for s in sums]
    th_probs = [ANALYTICAL[s] for s in sums]
    x = range(len(sums))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([i - width / 2 for i in x], mc_probs, width, label="Monte Carlo")
    ax.bar([i + width / 2 for i in x], th_probs, width, label="Аналітично")
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.set_xlabel("Сума")
    ax.set_ylabel("Ймовірність")
    ax.set_title("Ймовірності сум при киданні двох кубиків")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
  NUM_ROLLS = 1_000_000

  mc_probs = monte_carlo_simulation(NUM_ROLLS)
  print_comparison(mc_probs)
  plot_probabilities(mc_probs)


