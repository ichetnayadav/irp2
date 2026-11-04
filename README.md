# IRP2 - Programming Problems

**Name:** Chetna Yadav  
**Roll No:** 2481215

## Problems

| # | File | Description |
|---|------|-------------|
| 1 | `problems/p1_reverse_words.py` | Reverse the order of words in a sentence |
| 2 | `problems/p2_binary_search.py` | Binary search (no built-in search) |
| 3 | `problems/p3_digit_sum.py` | Sum of digits using recursion |
| 4 | `problems/p4_pair_count.py` | Count pairs with sum equal to k |

## How to Run

Each problem reads from **standard input**.

```bash
# Run a problem directly
python3 problems/p1_reverse_words.py

# Run with test input
python3 problems/p1_reverse_words.py < tests/p1_input.txt

# Verify output
python3 problems/p1_reverse_words.py < tests/p1_input.txt | diff - tests/p1_output.txt
```

## Project Structure

```
irp2/
├── README.md
├── .gitignore
├── problems/
│   ├── p1_reverse_words.py
│   ├── p2_binary_search.py
│   ├── p3_digit_sum.py
│   └── p4_pair_count.py
└── tests/
    ├── p1_input.txt
    ├── p1_output.txt
    ├── p2_input.txt
    ├── p2_output.txt
    ├── p3_input.txt
    ├── p3_output.txt
    ├── p4_input.txt
    └── p4_output.txt
```
