# Binary Search in Python

This project demonstrates a basic implementation of the binary search algorithm using Python. The program generates a sorted list of integers based on user input and selects a random number within that range. It then uses binary search to find the number and counts how many steps were taken to locate it.

---

## How It Works

1. The user is prompted to enter the lowest and highest values of a range.
2. A list of integers is created within that range.
3. A random number within the range is selected.
4. The binary search function is used to locate the random number in the list.
5. The result (index) and number of steps taken are printed to the screen.

---

## Binary Search Algorithm

Binary search works on sorted arrays by repeatedly dividing the search interval in half:

- Compare the target number to the middle element of the current search range.
- If it matches, return the index.
- If it is smaller, repeat the search on the left half.
- If it is larger, repeat the search on the right half.
- Continue until the number is found or the range is empty.

This algorithm has a time complexity of O(log n), making it efficient for large sorted lists.

---

## Example Output

The lowest value on the list is ? 1
The highest value on the list is ? 100
The secret number is: 47
The result is: 46 in 6 steps
