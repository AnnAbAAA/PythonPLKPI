# Напишіть програму, яка обчислює значення визначеної функції (на вхід подають дійсні числа).
#Залежно від вибору користувача обчислити площу круга, прямокутника або трикутника.
#Для обчислення площі кожної фігури повинна бути написана окрема функція.

def s_circle(rad):
    s_circ = rad*rad*3.14
    return s_circ

def s_rectangle(side1, side2):
    s_rec = side1*side2
    return s_rec

def s_triangle(side, height):
    s_tr = side*height*0.5
    return s_tr

x = int(input("Площа круга - 1, площа прямокутника - 2, площа трикутника - 3: "))
if x == 1:
    r = float(input("radius - ?: "))
    s = s_circle(r)
    print(s)
elif x == 2:
    s1 = float(input("side1 - ?: "))
    s2 = float(input("side2 - ?: "))
    s = s_rectangle(s1, s2)
    print(s)
elif x == 3:
    s1 = float(input("side - ?: "))
    h = float(input("height - ?: "))
    s = s_triangle(s1, h)
    print(s)
else:
    print("error")

