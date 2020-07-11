

def fibonaci_series(n):
    a = []
    a.append(1)
    a.append(1)
    if n < 1:
        return -1
    elif n <= 2:
        return [1] if n == 1 else a
    else:
        a0 = 1
        a1 = 1
        for i in range(2,n):
            sum = a0 + a1
            a.append(sum)
            a0,a1 = a1, sum
        return a


res = fibonaci_series(15)
print(res)