n = int(input('Number - ?: '))
found = False

for i in range(n):
    for d in range(n):
        if i**3 + d**3 == n:
            print(i, d)
            found = True

if not found:
    print('impossible')
