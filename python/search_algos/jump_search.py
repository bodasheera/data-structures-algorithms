import math


def jump_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    elif x < arr[0] or x > arr[n-1]:
        return -1
    else:
        # element has to be there in array
        m = round(math.sqrt(n))
        i = 0
        for i in range(0,n,i+m):
            if arr[i] >= x:
                break
        j = 0
        if arr[i] >= x:
            if arr[i] == x:
                return i
            else:
                for j in range(i-m,i):
                    if arr[j] == x:
                        break
                return j
        else:
            i = i - m
            for j in range(i+1,n):
                if arr[j] == x:
                    break
            return j


arr = list(range(1,101))
result = jump_search(arr,100)
print(result)