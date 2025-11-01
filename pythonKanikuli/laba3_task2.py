def decr(n):
    lst = []
    while n < 10000000:
        s = str(n)
        if s[0] > s[1] > s[2] > s[3] > s[4] > s[5] > s[6]:
            lst.append(n)
        n += 1
    return lst

def three(lst):
    result_lst = []
    for i in range(0,len(lst)):
        if lst[i] % 3 == 0:
            result_lst.append(lst[i])
    return result_lst

nums = decr(1000000)
result = three(nums)
print(result)
print(len(result))
