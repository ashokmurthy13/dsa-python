
# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
def binary_search(array, target):
    return binary_search_helper(array, target, 0, len(array)-1)


def binary_search_helper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if potential_match == target:
        return middle
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle - 1)
    else:
        return binary_search_helper(array, target, middle + 1, right)


print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
