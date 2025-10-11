a = input("Enter year ")

if len(a) != 4:
        print(0)
else:
    try:
        if(int(a) % 100 == 0):
           print((int(a)//100))
        else:
            print((int(a)//100)+1)
    except:
        print(0)
