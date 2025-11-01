#Написати програму, яка для заданого натурального числа N (100&lt;=N&lt;=999999) визначає, чи
#утворюють його цифри арифметичну прогресію. Передбачається, що в числі не менше трьох цифр.

import random
n = random.randint(100, 9999)
print(n)
s = str(n)
dif = int(s[1])-int(s[0])
works = True
for i in range(2, len(s)):
    if int(s[i]) - int(s[i-1]) != dif:
        works = False
        break
if works:
    print("Yes")
else:
    print("No")
