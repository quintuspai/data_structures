
#InterpolationSearch() -> uniformarly distributed list-> sort it
def interpolation_Search(arr , item : int) -> str():
    arr = sorted(arr)
    pos = -1
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = low + (high - low)*int((item-arr[low])/(arr[high]-arr[low]))
        if item == arr[mid]:
            pos = mid
            break
        elif item > arr[mid]:
            low = mid +1
        else:
            high = mid - 1
    if pos == -1:
        return 'The element {} was not found'.format(item)
    else:
        return 'The element was found at {}'.format(pos)
 
if __name__ == "__main__":
    *arr_list, item = input().split()
    arr_list = list(map(int, arr_list))
    print(interpolation_Search(arr_list, int(item)))
    