#реалізувати процедуру яка повертає століття року введення. Введення завжди має бути 4-значним рядком, якщо ні –
#повертає 0

a = input("Enter year ")

if len(a) != 4:
        print(0)
else:
    try:
        if(int(a) % 100 == 0):
           print(str((int(a)//100)) + "th")
        else:
            print(str((int(a)//100)+1) + "th")
    except:
        print(0)
