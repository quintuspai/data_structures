def merge(arr, beg, mid, end):
    i = beg
    j = mid+1
    index = beg
    temp = []
    while i<=mid and j <=end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1
        index = index + 1
    while j <= end:
        temp.append(arr[j])
        j = j + 1
        index = index + 1
    while i <= mid:
        temp.append(arr[i])
        i = i + 1
        index = index + 1
    key = beg
    for k in range(len(temp)):
        arr[key] = temp[k]
        key = key +1

def merge_sort(arr,beg,end):
    if beg < end:
        mid = (beg+end)//2
        merge_sort(arr, beg, mid)
        merge_sort(arr, mid+1, end)
        merge(arr,beg, mid, end)

if __name__ == "__main__":
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    merge_sort(arr_list, 0, len(arr_list)-1)
    print("After sorting {}".format(arr_list))