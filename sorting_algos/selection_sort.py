

def selection_sort(arr):
    n = len(arr)

    for i in range(0,n):
        small = arr[i]
        small_index = i
        for j in range(i,n):
            if arr[j] < small:
                small = arr[j]
                small_index = j
        arr[i],arr[small_index] = arr[small_index],arr[i]

    return arr

arr = [1,15,30,42,21,11,0]
res = selection_sort(arr)
print(res)