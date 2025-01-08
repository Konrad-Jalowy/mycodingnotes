def quick_sort(arr):
    _quick_sort(arr, 0, len(arr)-1)

def _quick_sort(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        _quick_sort(arr, first, splitpoint-1)
        _quick_sort(arr, splitpoint+1, last)

def partition(arr, first, last):
    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark+=1
        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark-=1
        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]
    arr[first], arr[rightmark] = arr[rightmark], arr[first]
    return rightmark

array1 = [100,-3,2,4,6,9,1,2,5,3,23]
quick_sort(array1)
print(array1)