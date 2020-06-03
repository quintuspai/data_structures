#Bubble Sorting
def bubble_sort(arr, n):
    for i in range(0,n-2):
        for j in range(i+1,n):
            if arr[i] > arr [j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
 
#Insertion sort
def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while ((temp <= arr[j]) and (j >= 0)):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

#------------------------------------

#Selection Sort
def smallest(arr, k ,n):
    small = arr[k]
    pos = k
    for j in range(k+1,n):
        if small > arr[j]:
            small = arr[j]
            pos = j
    return pos

def selection_sort(arr):
    n = len(arr)
    for k in range(n):
        pos = smallest(arr, k, n)
        temp = arr[k]
        arr[k] = arr[pos]
        arr[pos] = temp

#------------------------------------

#Merge Sort
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

#-----------------------------------------

#Quick sort
def partition(arr, beg, end):
    loc = left = beg
    right = end
    flag = 0
    while flag != 1:
        while arr[loc] <= arr[right] and (loc != right):
            right = right - 1
        if loc == right:
            flag = 1
        if arr[loc] > arr[right]:
            temp = arr[loc]
            arr[loc] = arr[right]
            arr[right] = temp
            loc = right
        if flag != 1:
            while arr[loc] > arr[left] and (loc != left):
                left = left + 1
            if loc == left:
                flag = 1
            if arr[loc] < arr[left]:
                temp = arr[left]
                arr[left] = arr[loc]
                arr[loc] = temp
                loc = left
    return loc     

def quick_sort(arr, beg, end):
    if beg < end:
        pivot = partition(arr, beg, end)
        quick_sort(arr, beg, pivot - 1)
        quick_sort(arr, pivot + 1, end)

#----------------------------------------------------------

if __name__ == "__main__":
    arr_list = list(map(int, input().split()))
    print("Before sorting {}".format(arr_list))
    quick_sort(arr_list, 0, len(arr_list) - 1)
    print("After sorting {}".format(arr_list))