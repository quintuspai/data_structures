#searching

#LinearSearch
def linear_Search(n : int, arr, item : int) -> str():
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
        return "Eelement found at {}".format(pos)

#InterpolationSearch() -> uniformarly distributed list-> sort it
def interpolation_Search(n : int, arr , item : int) -> str():
    arr = sorted(arr)
    pos = -1
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = low + (high - low)*int((item-arr[low])/(arr[high]-arr[low]))
        print(mid)
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
    
#JumpSeacth
def jump_Search(n : int, arr, item : int) -> str():
    import math
    step = int(math.floor((math.sqrt(n))))
    arr = sorted(arr)
    pos = -1
    low = 0
    high = n-1
    i = 0
    while i < step:
        if item < arr[step]:
            high = step - 1
        else:
            low = step + 1
        i = i + 1
    for i in range(low,high+1):
        print(arr[i])
        if arr[i] == item:
            pos = i
            break
    if pos == -1:
        return "Element {} not found".format(item)
    else:
        return "Element found at {}".format(pos) 

if __name__ == "__main__":
    n, *arr_list, item = input().split()
    arr_list = list(map(int, arr_list))
    print(jump_Search(int(n), arr_list, int(item)))
    