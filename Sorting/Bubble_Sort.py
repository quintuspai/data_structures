def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    bubble_sort(arr_list, len(arr_list))
    print("After sorting : {}".format(arr_list))