#10. Визначити середнє арифметичне елементів списку.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(0,20))

sum = 0

for i in range(0,len(lst)):
    sum = sum + lst[i]

average = sum / len(lst)

print(lst)
print(average)
