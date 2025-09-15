x = int(input("number: "))
d = True

for i in range(2, x):
    if x % i == 0:
        d = False
        break
print(d)
