"""
Problem 2: Binary Search
Given n sorted integers and a target, find the 0-based index using binary search.
No built-in search functions allowed.

Input:
    Line 1: n (number of elements)
    Line 2: n sorted integers (space-separated)
    Line 3: target value

Output:
    0-based index of target, or -1 if not found

Example:
    Input:  5 / 1 3 5 7 9 / 7
    Output: 3
"""


def binary_search(arr, target):
    """Perform binary search and return 0-based index or -1."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    result = binary_search(arr, target)
    print(result)


if __name__ == "__main__":
    main()
