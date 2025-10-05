#8. Сформувати список квадратів усіх елементів.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(-100,100))

lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i]*lst[i])

print(lst)
print(lst2)
