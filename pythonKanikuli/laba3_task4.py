import turtle as t
import random

def circle(size):
    t.circle(size)

def triangle(size):
    for _ in range(3):
            t.forward(size)
            t.left(120)
    
def square(size):
    for _ in range(4):
            t.forward(size)
            t.right(90)
    

n = int(input("Кількість фігур: "))

for i in range(n):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    
    shape = random.randint(1,3)
    sizeFigure = random.randint(20, 80)
    
    if shape == 1:
        circle(sizeFigure)
    elif shape == 2:
        triangle(sizeFigure)
    else:
        square(sizeFigure)
        
t.done()
