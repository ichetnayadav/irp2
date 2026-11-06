"""
Problem 4: Count Pairs with Given Sum
Given n integers and a target sum k, count the number of pairs (i, j)
where i < j and arr[i] + arr[j] == k.

Input:
    Line 1: n and k (space-separated)
    Line 2: n integers (space-separated)

Output:
    Number of pairs whose sum equals k

Example:
    Input:  5 6
           1 2 3 4 5
    Output: 2
    Explanation: pairs (1,5) and (2,4) sum to 6
"""


def count_pairs(arr, k):
    """Count pairs (i, j) with i < j whose sum equals k."""
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1

    return count


def main():
    first_line = input().split()
    n = int(first_line[0])
    k = int(first_line[1])

    arr = list(map(int, input().split()))

    result = count_pairs(arr, k)
    print(result)


if __name__ == "__main__":
    main()
