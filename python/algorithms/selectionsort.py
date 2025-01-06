def selection_sort(arr):
    for i in range(0, len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[lowest] > arr[j]:
                lowest = j
        if i != lowest:
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr

print(selection_sort([2,1,9,76,4]))