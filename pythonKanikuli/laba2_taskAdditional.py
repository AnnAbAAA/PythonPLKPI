max = 14
for a in range(1, max+1):
    for b in range(1, max+1):
        for c in range(1, max+1):
            if a + b - 9 == 4 and a - b * c == 4 and a + b - c == 4:
                print(a, b, c)
