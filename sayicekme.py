import numpy as np
import turtle

def draw_random_numbers(first, second, count):
    pencere = turtle.Screen()
    pencere.bgcolor("black")
    pencere.setup(width=800, height=600)
    pencere.title("Rastgele Sayılar")

    for _ in range(count):
        x = np.random.randint(-400, 400)
        y = np.random.randint(-300, 300)
        rs = np.random.randint(first, second)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("white")  # Yazı rengini beyaz yapabilirsiniz.
        turtle.write(rs, align="center", font=("Arial", 24, "bold"))

    turtle.done()

def main():
    first = int(input("Hangi sayıdan: "))
    second = int(input("Hangi sayıya kadar: "))
    count = int(input("Kaç tane rastgele sayı üretmek istiyorsunuz?"))

    draw_random_numbers(first, second, count)
    turtle.hideturtle
if __name__ == "__main__":
    main()
