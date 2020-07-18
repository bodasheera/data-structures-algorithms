
def binary_search(a,number):
    if len(a) == 0:
        print("array is empty")
        return

    high = len(a)-1
    low = 0

    found = False

    while high >= low:
        middle = int((high + low) / 2)

        if a[middle] == number:
            found = True
            break

        elif a[middle]> number:
            high = middle - 1

        elif a[middle] < number:
            low = middle + 1

    if found is True:
        print(f"array is {a}")
        print(f"Number {number} found at position {middle + 1}")
    else:
        print(f"array is {a}")
        print(f"Number {number} not found")


def binary_search_recursive(a,number,low , high):
    if high >= low:
        mid = int((low + high)/2)
        if a[mid] == number:
            return f"Number found at {mid+1}"
        elif a[mid] > number:
            res = binary_search_recursive(a,number,low , mid-1)
        elif a[mid] < number:
            res = binary_search_recursive(a,number,mid + 1 , high)

    if low > high:
        res = "Not Found"

    return res


a = [1,2,3,4,5,6]
number = 5

low = 0
high = len(a)-1
res = binary_search_recursive(a,number,low,high)
print(res)