def binary_search(array, target):
    return _binary_search(array, target, 0, len(array)-1)

def _binary_search(array, target, left, right):
    if left > right:
        return -1
    middle = (left+right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return _binary_search(array, target, left, middle - 1)
    else:
        return _binary_search(array, target, middle + 1, right)


print(binary_search([1,2,3], 2))