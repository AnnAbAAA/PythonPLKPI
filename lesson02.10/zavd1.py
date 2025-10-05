#Створити список з 10 випадкових чисел. Знайти їх суму.

import random

lst=[]
for i in range(5):
    lst.append(random.randint(1,5))
    
sum = 0
for i in range(0,len(lst)):
    sum = sum + lst[i]

print(lst)
print("Sum: ", sum)
