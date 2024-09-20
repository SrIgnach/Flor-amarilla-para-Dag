from turtle import *
import math

tracer(2) 
h = 0
bgcolor('purple')  
pensize(3)  
color('yellow')
speed(9)  

for i in range(400):
    h += 0.006
    lt(179)
    backward(i * 0.03)  
    circle(i * 0.15, 120) 
    rt(14)
    forward(i * 0)  
    circle(i * 0.15, 120)  

shape('turtle')
pencolor('grey')
fillcolor('black')
phi = 137.508 * (math.pi / 180.0)
for i in range(300):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

penup()
goto(-175, -300)  
pencolor('white')
write("Feliz 21 de sep Dag, TQM :)", font=("Century Gothic", 21, "bold"))

penup()
goto(-250, 250)  
pencolor('grey')
write("MI AMIGA NO SERÁ ESPECTADORA", font=("Century Gothic", 25, "bold"))

penup()
goto(500, 500)  
pencolor('green')
write("MI AMIGA NO SERÁ ESPECTADORA", font=("Century Gothic", 25, "bold"))

done()