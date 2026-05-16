# Завдання 3

# Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
# Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють
# сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq

def min_cost_to_connect_cables(lengths):
    if len(lengths) <= 1:
        return 0

    heap = lengths[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        cost = a + b
        total_cost += cost

        heapq.heappush(heap, cost)

    return total_cost


# Тест
print(min_cost_to_connect_cables([2, 8, 5, 12]))


def knapSack(W, wt, val, n):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        print(K)
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# виклик функції
print(knapSack(capacity, weight, value, n))  # 220
