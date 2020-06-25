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
        if arr[i] == item:
            pos = i
            break
    if pos == -1:
        return "Element {} not found".format(item)
    else:
        return "Element found at {}".format(pos) 

if __name__ == "__main__":
    *arr_list, item = input().split()
    arr_list = list(map(int, arr_list))
    print(jump_Search(len(arr_list), arr_list, int(item)))