import turtle
import time
import random

# Pencere ayarları
pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("black")
pencere.setup(width=600, height=600)
pencere.tracer(0)  # Animasyonu kapat

# Yılanın başlangıç konumu ve hareketleri
baslik = turtle.Turtle()
baslik.speed(0)
baslik.color("white")
baslik.penup()
baslik.hideturtle()
baslik.goto(0, 260)
baslik.write("Yılan Oyunu", align="center", font=("Courier", 24, "normal"))

yilan = turtle.Turtle()
yilan.speed(0)
yilan.shape("square")
yilan.color("white")
yilan.penup()
yilan.goto(0, 0)
yilan.direction = "stop"

# Yem oluştur
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0, 100)

yemekler = []

# Yılanın hareket fonksiyonları
def yilan_hareket():
    if yilan.direction == "up":
        y = yilan.ycor()
        yilan.sety(y + 20)
    if yilan.direction == "down":
        y = yilan.ycor()
        yilan.sety(y - 20)
    if yilan.direction == "left":
        x = yilan.xcor()
        yilan.setx(x - 20)
    if yilan.direction == "right":
        x = yilan.xcor()
        yilan.setx(x + 20)

# Yılanın yön değiştirmesi
def yukari():
    if yilan.direction != "down":
        yilan.direction = "up"

def asagi():
    if yilan.direction != "up":
        yilan.direction = "down"

def sola():
    if yilan.direction != "right":
        yilan.direction = "left"

def saga():
    if yilan.direction != "left":
        yilan.direction = "right"

# Tuşlara tepki verme
pencere.listen()
pencere.onkey(yukari, "Up")
pencere.onkey(asagi, "Down")
pencere.onkey(sola, "Left")
pencere.onkey(saga, "Right")

# Oyun döngüsü
while True:
    pencere.update()

    # Yem yılanla çarpışırsa
    if yilan.distance(yem) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        yem.goto(x, y)

        yeni_yemek = turtle.Turtle()
        yeni_yemek.speed(0)
        yeni_yemek.shape("circle")
        yeni_yemek.color("red")
        yeni_yemek.penup()
        yemekler.append(yeni_yemek)

    # Yılanın kuyruğunu güncelleme
    for index in range(len(yemekler) - 1, 0, -1):
        x = yemekler[index - 1].xcor()
        y = yemekler[index - 1].ycor()
        yemekler[index].goto(x, y)

    if len(yemekler) > 0:
        x = yilan.xcor()
        y = yilan.ycor()
        yemekler[0].goto(x, y)

    yilan_hareket()

    # Yılanın kendine çarpıp çarpmadığını kontrol etme
    for yemek in yemekler:
        if yilan.distance(yemek) < 20:
            time.sleep(1)
            yilan.goto(0, 0)
            yilan.direction = "stop"

            for yemek_sil in yemekler:
                yemek_sil.goto(1000, 1000)

            yemekler.clear()

    time.sleep(0.1)
