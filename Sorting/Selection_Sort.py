def smallest(arr, k ,n):
    small = arr[k]
    pos = k
    for j in range(k+1,n):
        if small > arr[j]:
            small = arr[j]
            pos = j
    return pos

def selection_sort(arr):
    n = len(arr)
    for k in range(n):
        pos = smallest(arr, k, n)
        temp = arr[k]
        arr[k] = arr[pos]
        arr[pos] = temp

if __name__ == '__main__':
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    selection_sort(arr_list)
    print("After sorting {}".format(arr_list))