import math

def is_prime(n):
    i = 0
    prime = True

    if n == 1 or n % 2 == 0:
        return False

    for i in range(3,round(math.sqrt(n))+1, i+2):
        if n % i == 0:
            prime = False
    return prime


for i in range(1,100):
    if is_prime(i):
        print(i)
