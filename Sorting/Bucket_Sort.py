def insertion_sort(sub_list):
    for i in range(len(sub_list)):
        temp = sub_list[i]
        j = i - 1
        while (temp > arr[j]) and (j >= 0):
            sub_list[j + 1] = sub_list[j]
            j -= 1
        sub_list[j + 1] = temp
    return sub_list
            

def bucket_sort(arr, n):
    bucket = [[] for _ in range(n)]
    for i in range(n):
        bucket[int(n * arr[i])].append(arr[i])
    for i in range(len(bucket)):
        insertion_sort(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr
    

if __name__ == "__main__":
    #arr = list(map(int, input().split()))
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(bucket_sort(arr, len(arr)))