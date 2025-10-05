#9. Вивести індекси всіх елементів, які дорівнюють мінімальному.

import random

lst=[]
for i in range(15):
    lst.append(random.randint(0,5))

lst2 = []

for i in range(0,len(lst)):
    if lst[i] == min(lst):
        lst2.append(i)
        
print(lst)
print(lst2)
