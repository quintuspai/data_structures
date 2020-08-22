def max_heapify(arr, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)
    
def heap_sort(arr):
    #Build max_heap
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, i)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0)


if __name__ == "__main__":
    #arr = list(map(int, input().split()))
    arr = [10, 3, 76, 34, 23, 32]
    heap_sort(arr)
    print("After sorting : {}".format(arr))
    