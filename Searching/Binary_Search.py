#BinarySearch
def binary_Search(n : int, arr, item : int) -> str():
    arr = sorted(arr)
    pos = -1
    beg = 0
    end =  n
    while beg <= end:
        mid = int((beg + end)/2)
        if arr[mid] == item:
            pos = mid + 1
            break
        elif arr[mid] > item:
            end = mid - 1
        else:
            beg = mid + 1
    if pos == -1:
        return "Element {} not found.".format(item)
    else:
        return "Element found at {}".format(pos)

if __name__ == "__main__":
    *arr_list, item = input().split()
    arr_list = list(map(int, arr_list))
    print(binary_Search(len(arr_list), arr_list, int(item)))
    