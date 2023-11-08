import turtle
import random
import math

# Pencere oluştur
pencere = turtle.Screen()
pencere.title("Top Çarpışma Simülasyonu")
pencere.bgcolor("black")
pencere.setup(width=800, height=600)

# Toplar listesi
toplar = []

# Top sınıfı
class Top(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-390, 390), random.randint(-290, 290))
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

# Topları oluştur
top_sayisi = 10
for _ in range(top_sayisi):
    top = Top()
    toplar.append(top)


# Topların hareketi
while True:
    pencere.update()

    for top in toplar:
        top.setx(top.xcor() + top.dx)
        top.sety(top.ycor() + top.dy)

        # Sınırları kontrol et
        if top.xcor() > 390 or top.xcor() < -390:
            top.dx *= -1
        if top.ycor() > 290 or top.ycor() < -290:
            top.dy *= -1

    # Topların birbirleriyle çarpışmasını kontrol et
    for i in range(len(toplar)):
        for j in range(i + 1, len(toplar)):
            top1 = toplar[i]
            top2 = toplar[j]
            mesafe = math.sqrt((top1.xcor() - top2.xcor())**2 + (top1.ycor() - top2.ycor())**2)

            if mesafe < 20:
                top1.color("yellow")
                top2.color("blue")
                # Çarpışma durumunda hızları ikiye katla
                top1.dx *= 2
                top1.dy *= 2
                top2.dx *= 2
                top2.dy *= 2

    # Hızlı hareket etmek için beklemek
    turtle.delay(0)
