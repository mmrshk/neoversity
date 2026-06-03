# Завдання 6. Жадібні алгоритми та динамічне програмування

# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм
# динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах
# обмеженого бюджету.

# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника,
# де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення
# калорій до вартості, не перевищуючи заданий бюджет.

# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming,
# яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.


ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

class Item:
    def __init__(self, cost, calories):
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items: list[Item], capacity: int) -> int:
    items_sorted = sorted(items, key=lambda x: x[1].ratio, reverse=True)

    selected: list[str] = []
    total_calories = 0
    total_cost = 0

    for name, item in items_sorted:
        if capacity >= item.cost:
            capacity -= item.cost
            total_cost += item.cost
            total_calories += item.calories

            selected.append(name)

    return selected, total_calories, total_cost


def dynamic_programming(budget: int, items_dict: dict) -> tuple[list[str], int, int]:
    names = list(items_dict.keys())
    weights = [items_dict[name]["cost"] for name in names]
    calories = [items_dict[name]["calories"] for name in names]
    num_items = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for current_budget in range(budget + 1):
            if weights[i - 1] <= current_budget:
                dp[i][current_budget] = max(
                    calories[i - 1] + dp[i - 1][current_budget - weights[i - 1]],
                    dp[i - 1][current_budget],
                )
            else:
                dp[i][current_budget] = dp[i - 1][current_budget]

    selected: list[str] = []
    remaining_budget = budget

    for i in range(num_items, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            selected.append(names[i - 1])
            remaining_budget -= weights[i - 1]

    selected.reverse()
    total_calories = dp[num_items][budget]
    total_cost = sum(items_dict[name]["cost"] for name in selected)

    return selected, total_calories, total_cost


if __name__ == "__main__":
    items = [(name, Item(data["cost"], data["calories"])) for name, data in ITEMS.items()]
    capacity = 100

    g_dishes, g_cal, g_cost = greedy_algorithm(items, capacity)
    print("Greedy:")
    print("  dishes:", g_dishes)
    print("  total calories:", g_cal)
    print("  total cost:", g_cost)

    dp_dishes, dp_cal, dp_cost = dynamic_programming(capacity, ITEMS)
    print("\nDynamic programming:")
    print("  dishes:", dp_dishes)
    print("  total calories:", dp_cal)
    print("  total cost:", dp_cost)