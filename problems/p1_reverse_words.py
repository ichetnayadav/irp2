"""
Problem 1: Reverse Word Order
Read a sentence from standard input and print the words in reverse order.

Example:
    Input:  I love coding
    Output: coding love I
"""


def reverse_words(sentence):
    """Reverse the order of words in a sentence."""
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


def main():
    sentence = input()
    result = reverse_words(sentence)
    print(result)


if __name__ == "__main__":
    main()
