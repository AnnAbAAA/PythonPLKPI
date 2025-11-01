N = int(input("N "))
k = int(input("k "))
p1 = int(input("p1 "))
p2 = int(input("p2 "))

summ1 = N * p1

tot = (N + k - 1) // k
summ2 = tot * p2

ful = N // k
ost = N % k
summ3 = ful * p2 + ost * p1

ans = min(summ1, summ2, summ3)
print(ans)