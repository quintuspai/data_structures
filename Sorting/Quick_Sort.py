def partition(arr, beg, end):
    loc = left = beg
    right = end
    flag = 0
    while flag != 1:
        while arr[loc] <= arr[right] and (loc != right):
            right = right - 1
        if loc == right:
            flag = 1
        if arr[loc] > arr[right]:
            temp = arr[loc]
            arr[loc] = arr[right]
            arr[right] = temp
            loc = right
        if flag != 1:
            while arr[loc] > arr[left] and (loc != left):
                left = left + 1
            if loc == left:
                flag = 1
            if arr[loc] < arr[left]:
                temp = arr[left]
                arr[left] = arr[loc]
                arr[loc] = temp
                loc = left
    return loc     

def quick_sort(arr, beg, end):
    if beg < end:
        pivot = partition(arr, beg, end)
        quick_sort(arr, beg, pivot - 1)
        quick_sort(arr, pivot + 1, end)

if __name__ == "__main__":
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    quick_sort(arr_list, 0, len(arr_list) - 1)
    print("After sorting {}".format(arr_list))