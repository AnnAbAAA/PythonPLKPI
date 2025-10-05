#6. Порахувати кількість чисел, що більші за 5.

import random

lst=[]
for i in range(10):
    lst.append(random.randint(-100,100))

sum = 0
for i in range(0, len(lst)):
    if lst[i]>5:
        sum = sum+1
        
print(lst)
print(sum)
