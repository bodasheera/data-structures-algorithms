

def collatz_conjucture(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz_conjucture(n/2)
    elif n % 2 != 0:
        return 1 + collatz_conjucture(3*n + 1)

for i in range(1,20):
    print(f"It takes {collatz_conjucture(i)} steps to reach from {i} to 1")