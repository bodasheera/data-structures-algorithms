
def bubble_sort(arr):
    i,j = 0,0
    n = len(arr)

    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr


arr = [1,5,3,4,2,10,0]
res = bubble_sort(arr)
print(res)