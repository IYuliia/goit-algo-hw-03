import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
   
    screen = turtle.Screen()
    screen.bgcolor("lightpink")
    
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 90)  
    t.pendown()

   
    order = int(input("Введіть рівень рекурсії для фракталу Коха (наприклад, 3): "))
  
    koch_snowflake(t, order, 300)
    
    screen.exitonclick()


if __name__ == "__main__":
    main()
