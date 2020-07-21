def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    smallest_val = 0
    middle_val = 0
    largest_val = len(arr) - 1

    while smallest_val <= largest_val:
        middle_val = (largest_val + smallest_val) // 2

        if arr[middle_val] < target:
            smallest_val = middle_val + 1

        elif arr[middle_val] > target:
            largest_val = middle_val - 1

        else:
            return middle_val

    return -1  # not found
