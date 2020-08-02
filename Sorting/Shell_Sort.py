def shell_sort(arr):
    flag = 1
    n = len(arr)
    gap_size = n
    while (flag == 1) or (gap_size > 1):
        flag = 0
        gap_size = (gap_size) // 2
        for i in range(0,(n - gap_size)):
            if arr[gap_size + i] < arr[i]:
                arr[gap_size + i], arr[i] = arr[i], arr[gap_size + i]
        
if __name__ == "__main__":
    #arr = list(map(int,input().split()))
    arr=[63, 19, 7, 90, 81, 36, 54, 45, 72, 27, 22, 9, 41, 59, 33]
    shell_sort(arr)
    print("After sorting : {}".format(arr))