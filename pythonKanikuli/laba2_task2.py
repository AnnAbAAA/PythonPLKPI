w = int(input("Ширина: "))
h = int(input("Висота: "))
outline = input("Контур: ")
fill = input("Заливка: ")

for i in range(h):
    if i == 0 or i == h-1:
        print(outline*w)
    else:
        print(outline + fill*(w-2) + outline)