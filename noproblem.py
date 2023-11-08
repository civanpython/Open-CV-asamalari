import numpy as np
import turtle

pencere = turtle.Screen()
pencere.bgcolor("black")
pencere.setup(width=800,height=600)
pencere.title("Sayi uretme")


first = int(input("Hangi sayıdan: "))
second = int(input("Hangi sayıya kadar: "))
third = int(input("Kaç tane rastgele sayı üretmek istiyorsunuz?"))



rs = np.random.randint(first,second,third)

kalem = turtle.Turtle()
kalem.penup()
kalem.hideturtle()
kalem.goto(0, 0)

kalem.write(""rs,align="center",font=("Arial",24,"bold"))

pencere.mainloop()