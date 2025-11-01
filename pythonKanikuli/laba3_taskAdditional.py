def lucky_tickets(a1, a2):
    count = 0
    for i in range(a1, a2 + 1):
        s = str(i)
        while len(s) < 6:
            s = "0" + s
        first = int(s[0]) + int(s[1]) + int(s[2])
        last = int(s[3]) + int(s[4]) + int(s[5])
        if first == last:
            count += 1
    return count


a1 = int(input("a1 = "))
a2 = int(input("a2 = "))

print("Кількість щасливих квитків:", lucky_tickets(a1, a2))
