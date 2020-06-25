#Insertion sort
def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while ((temp <= arr[j]) and (j >= 0)):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp


if __name__ == "__main__":
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    insertion_sort(arr_list, len(arr_list))
    print("After sorting {}".format(arr_list))