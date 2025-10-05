#5. Вивести елементи списку у зворотному порядку.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(1,100))

lst2=[]
for i in range(len(lst)):
    lst2.append(lst[-i-1])
    
print(lst)
print(lst2)
