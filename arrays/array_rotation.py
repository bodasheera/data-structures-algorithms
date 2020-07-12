

# using python easy method
def array_rotation(arr,k):
    n = len(arr)

    if k == 0:
        return arr
    else:
        if k > n:
            k = k % n
        return arr if k == 1 else arr[k:n] + arr[0:k]


# c++ simple way store first k value in temp. shift remaining k steps back . append first k to end of array
def array_rotation_1(arr,k):
    n = len(arr)

    if k == 0:
        return arr
    else:
        if k > n:
            k = k % n
        temp = []
        for i in range(0,k):
            temp.append(arr[i])

        for i in range(k,n):
            arr[i-k] = arr[i]
        j = 0
        for i in range(n-k,n):
            arr[i] = temp[j]
            j += 1

        return arr


# shift one at a time
def array_rotation_2(arr,k):
    n = len(arr)

    if k == 0:
        return arr
    else:
        if k > n:
            k = k % n
        for i in range(0,k):
            temp = arr[0]
            for j in range(1,n):
                arr[j-1] = arr[j]
            arr[n-1] = temp
        return arr


arr = [1,2,3,4,5]
print(array_rotation_2(arr,11))