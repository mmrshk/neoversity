import math
import sys
import turtle


def koch_curve(t: turtle.Turtle, order: int, length: float) -> None:
    if order == 0:
        t.forward(length)
        return

    third = length / 3.0

    koch_curve(t, order - 1, third)
    t.left(60)
    koch_curve(t, order - 1, third)
    t.right(120)
    koch_curve(t, order - 1, third)
    t.left(60)
    koch_curve(t, order - 1, third)


def draw_koch_snowflake(order: int, side: float = 360.0) -> None:
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха (рівень рекурсії {order})")
    screen.setup(width=900, height=900)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("steelblue")
    t.pensize(1)
    t.penup()
    t.goto(-side / 2, -side * math.sqrt(3) / 6)
    t.setheading(0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, side)
        t.right(120)

    t.hideturtle()
    screen.update()
    screen.exitonclick()


def read_recursion_level() -> int:
    while True:
        raw = input("Введіть рівень рекурсії (ціле число ≥ 0, порожньо — 3): ").strip()
        if raw == "":
            return 3
        try:
            order = int(raw)
        except ValueError:
            print("Потрібне ціле число.", file=sys.stderr)
            continue
        if order < 0:
            print("Рівень не може бути від’ємним.", file=sys.stderr)
            continue
        return order


def main() -> None:
    order = read_recursion_level()
    if order > 7:
        print("Увага: великий рівень рекурсії може довго малюватися.", file=sys.stderr)

    try:
        draw_koch_snowflake(order)
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
