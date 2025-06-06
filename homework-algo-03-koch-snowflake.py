import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(level):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, 300, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0-6): "))
        if level < 0 or level > 6:
            print("Рівень має бути від 0 до 6.")
        else:
            draw_snowflake(level)
    except ValueError:
        print("❌ Будь ласка, введіть ціле число.")