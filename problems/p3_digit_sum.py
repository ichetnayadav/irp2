"""
Problem 3: Digit Sum Using Recursion
Calculate the sum of digits of a number using recursion only.

Input:
    A single integer

Output:
    Sum of its digits

Example:
    Input:  9875
    Output: 29
"""


def digit_sum(n):
    """Calculate sum of digits recursively."""
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)


def main():
    number = int(input())
    result = digit_sum(number)
    print(result)


if __name__ == "__main__":
    main()
