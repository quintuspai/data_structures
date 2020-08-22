def counting_sort(arr):
    counts = [0] * (max(arr) + 1)
    for i in arr:
        counts[i] += 1
    index = 0
    for i, count in enumerate(counts):
        counts[i] = index
        index += count
    sorted_list = [None] * (len(arr))
    for item in arr:
        sorted_list[counts[item]] = item
        counts[item] +=1
    return sorted_list
    
if __name__ == "__main__":
    #arr = list(map(int, input().split()))
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("After Sorting : {}".format(counting_sort(arr)))