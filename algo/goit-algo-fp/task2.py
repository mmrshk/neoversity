# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
# Необхідно написати програму на Python, яка використовує рекурсію для створення
# фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати
# можливість вказати рівень рекурсії.

import math
import turtle

MAX_LEVEL = 12
DEFAULT_LEVEL = 5
ANGLE = 45


def draw_square(t, size):
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()


def pythagoras_tree(t, size, level, angle=ANGLE):
    if level == 0:
        return

    draw_square(t, size)

    branch_size = size * math.cos(math.radians(angle))

    t.forward(size)
    t.left(angle)
    pythagoras_tree(t, branch_size, level - 1, angle)
    t.right(2 * angle)
    pythagoras_tree(t, branch_size, level - 1, angle)
    t.left(angle)
    t.backward(size)


def read_recursion_level():
    prompt = (
        f"Введіть рівень рекурсії (0–{MAX_LEVEL}, Enter = {DEFAULT_LEVEL}): "
    )
    raw = input(prompt).strip()

    if not raw:
        return DEFAULT_LEVEL

    try:
        level = int(raw)
    except ValueError:
        print(f"Некоректне значення, використовую {DEFAULT_LEVEL}.")
        return DEFAULT_LEVEL

    if level < 0:
        print("Рівень не може бути від'ємним, використовую 0.")
        return 0

    if level > MAX_LEVEL:
        print(f"Занадто великий рівень, обмежую до {MAX_LEVEL}.")
        return MAX_LEVEL

    return level


def main():
    level = read_recursion_level()

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")
    screen.setup(width=900, height=700)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.color("#2C5E3B")
    t.fillcolor("#8FBC8F")

    t.goto(-40, -250)
    t.setheading(90)

    pythagoras_tree(t, 80, level, ANGLE)

    t.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
