#3. Знайти максимальний елемент списку без `max()`.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(-100,100))
    
print(lst)

for i in range(len(lst)-1, 0, -1):
    if lst[i] < lst[i-1]:
        lst.pop(i)
    else:
        lst.pop(i-1)
print(lst)
