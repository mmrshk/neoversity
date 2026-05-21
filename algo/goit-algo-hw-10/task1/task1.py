# Завдання 1

# У конспекті ми розглянули приклад про розбиття суми на монети.
# Маємо набір монет [50, 25, 10, 5, 2, 1]. Уявіть, що ви розробляєте систему для касового апарату,
# яка повинна визначити оптимальний спосіб видачі решти покупцеві.
# Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

# 1. Функція жадібного алгоритму find_coins_greedy.
# Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми.
# Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.

# 2. Функція динамічного програмування find_min_coins.
# Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет,
# необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом.
# Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}

# Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування,
# базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах.
# Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях.
# Свої висновки додайте у файл readme.md домашнього завдання.

import timeit

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    coins_dictionary = {}

    for coin in sorted(COINS, reverse=True):
        count = amount // coin
        if count:
            coins_dictionary[coin] = count
            amount -= coin * count

    return coins_dictionary


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining = amount

    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return result

def run_case(amount: int, repeat: int = 1000) -> None:
    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount), number=repeat
    )

    dp_time = timeit.timeit(
        lambda: find_min_coins(amount), number=repeat
    )

    print(f"\n--- amount = {amount:,} (repeat={repeat}) ---")
    print(f"greedy: {greedy_result}")
    print(f"dp:     {dp_result}")
    print(f"match:  {greedy_result == dp_result}")
    print(f"greedy: {greedy_time:.6f} s total ({greedy_time / repeat * 1e6:.3f} µs per call)")
    print(f"dp:     {dp_time:.6f} s total ({dp_time / repeat * 1e6:.3f} µs per call)")

    if dp_time > 0:
        print(f"dp / greedy ≈ {dp_time / greedy_time:.1f}x")



if __name__ == "__main__":
    # Коректність на різних сумах
    for amount in [0, 1, 48, 113, 156]:
        g = find_coins_greedy(amount)
        d = find_min_coins(amount)
        print(f"amount={amount}: greedy={g}, dp={d}, equal={g == d}")

    # Час: малі суми — більше повторень, великі — менше
    run_case(113, repeat=10_000)
    run_case(10_000, repeat=1_000)
    run_case(100_000, repeat=100)
    run_case(1_000_000, repeat=10)

