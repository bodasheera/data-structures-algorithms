
def merge_sort(arr):
    n = len(arr)

    # base case
    if n == 1:
        return arr

    # recursive case
    half = round(n/2)
    left = merge_sort(arr[0:half])
    right = merge_sort(arr[half:n])

    merged_arr = []
    i = 0
    j = 0

    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        elif right[j] < left[i]:
            merged_arr.append(right[j])
            j += 1

    if i < len(left) and len(left[i:len(left)]) != 0:
        merged_arr = merged_arr + left[i:len(left)]
    elif j < len(right) and len(right[j:len(right)]) != 0:
        merged_arr = merged_arr + right[j:len(right)]
    return merged_arr


arr = [41,50,31,14,21,10,1000,11]
res = merge_sort(arr)
print(res)