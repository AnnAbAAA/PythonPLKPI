#7. Знайти добуток усіх елементів.

import random

lst=[]
for i in range(5):
    lst.append(random.randint(-100,100))

dob = 1
for i in range(0, len(lst)):
    dob = dob * lst[i]
print(lst)
print(dob)
