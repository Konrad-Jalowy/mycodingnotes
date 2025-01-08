def binary_search(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(binary_search([1,2,3], 4))