#4. Замінити всі від’ємні числа на `0`.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(-100,100))
    
print(lst)

for i in range(0, len(lst)):
    if lst[i]<0:
        lst[i] = 0
print(lst)

