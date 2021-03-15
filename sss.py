import time
import turtle
from distutils.core import setup
from turtle import *


input("Ingrese un valor en cm para los lados del cuadrado")
while True:

        try:
            A = int(input("A = "))
            B = int(input("B = "))
            C = int(input("C = "))
            D = int(input("D = "))
            break
        except:
            print("Eso es un caracter mas no una expresion numerica")

if A*B==C*B:
    print("Procediento a dibujar cuadrado")
else:
    print("Se dibujara un objeto irregular")
input("Bien, ahora ingrese la base y altura del rectangulo")
while True:

        try:
            A1 = int(input("La altura es = "))
            B1 = int(input("La base es = "))
            break
        except:
            print("Eso es un caracter, mas no una expresion numerica")

C1 = B1
D1 = A1

setup(1900, 1000, 0, 0)
screensize(4000, 4000)
turtle.setx(-500)
turtle.sety(400)
title("Creacion del Cuadrado y Rectangulo")
hideturtle()
bgcolor("black")
color('blue', 'purple')
begin_fill()
forward(A)
right(400//2-150+40)
forward(B)
right(5**3-35)
forward(C)
right(24**2/12+42)
forward(D)
end_fill()

time. sleep(2)
reset()
turtle.setx(-500)
turtle.sety(400)
begin_fill()
color('blue', 'purple')
hideturtle()
forward(B1)
right(4256%95+14)
forward(A1)
right(2500%123+50)
forward(C1)
right(40-100+210-120/2)
forward(D1)
right(51+213-127-235/5)
end_fill()
done()