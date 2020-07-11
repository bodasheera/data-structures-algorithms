

def fibonaci_series(n):
    a = []
    a.append(0)
    a.append(1)
    if n < 1:
        return -1
    elif n <= 2:
        return [0] if n == 1 else a
    else:
        a0 = 1
        a1 = 1
        for i in range(2,n):
            sum = a0 + a1
            a.append(sum)
            a0,a1 = a1, sum
        return a


def fibonacci_recursive(n):
    # base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


for i in range(1,10):
    print(fibonacci_recursive(i))