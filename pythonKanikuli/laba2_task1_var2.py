#Отримати всі числа, які не перевищують заданого числа N (10<N<9999) та діляться без
#залишку на всі свої цифри.

import random
n = random.randint(10, 9999)
lst=[]
print(n)
for i in range(1, n + 1):
    s = str(i)
    ok = True
    for ch in s:
        d = int(ch)
        if d == 0 or i % d != 0:
            ok = False
            break
    if ok:
        lst.append(i)

print(lst)