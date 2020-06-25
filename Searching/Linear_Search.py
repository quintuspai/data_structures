#LinearSearch
def linear_Search(arr, item : int) -> str():
    pos = -1
    i = 0
    while i in range(len(arr)):
        if arr[i] == item:
            pos = i+1
            break
        i = i + 1
    if pos == -1:
        return "Element {} not found".format(item)
    else:
        return "Element found at {}".format(pos)

if __name__ == "__main__":
    *arr_list, item = input().split()
    arr_list = list(map(int, arr_list))
    print(linear_Search(arr_list, int(item)))