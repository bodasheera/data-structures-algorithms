

def insertion_sort(arr):
    n = len(arr)
    j = 0
    i = 0
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            for j in range(i,0,-1):
                if arr[j] < arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]

    return arr


arr = [41,50,31,14,21,10,1000]
res = insertion_sort(arr)
print(res)