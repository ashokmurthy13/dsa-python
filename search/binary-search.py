
# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if potentialMatch == target:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
