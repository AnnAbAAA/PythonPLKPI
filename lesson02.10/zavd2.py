#Вивести всі парні елементи списку

import random

lst=[]
for i in range(10):
    lst.append(random.randint(1,100))

lst2=[]
for i in range(0,len(lst)):
    if lst[i] % 2 == 0:
        lst2.append(lst[i])

print(lst)
print(lst2)
