#Розробити модуль що містить функції для перетворення десяткового числа в двійкове та
#двійкового числа в десяткове.

def y_decyat(num):
    s = str(num)
    sum = 0
    a = 0
    for i in range(len(s) - 1, -1, -1):
        sum += int(s[i]) * (2 ** a)
        a += 1
    return sum

def y_dviik(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s


opt = int(input("У десяткове - 1, у двійкове - 2: "))
n = int(input("num - ?: "))

if opt == 1:
    a = y_decyat(n)
    print(a)
elif opt == 2:
    a = y_dviik(n)
    print(a)
else:
    print('error')