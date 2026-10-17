# Python Lists, Palindrome Checking, and Tuples
## Complete Beginner-Friendly Notes

**Purpose:** These notes explain every topic and code line in the accompanying practice program. They are written for a beginner learning Python. Read each section, run the examples, and try to predict the output before running the code.

---

# 1. What Is a List?

A **list** is a Python data type that stores multiple items in a single variable. Lists use square brackets `[]`, and commas separate the items.

```python
marks = [1, 2, 3, 4, 5]
names = ["Aarav", "Riya", "Kabir"]
mixed = [10, "Python", 3.5, True]
```

A list can store integers, strings, decimal numbers, Boolean values, or a mixture of data types.

## Main characteristics of lists

- **Ordered:** Items keep their positions in the list.
- **Mutable:** Items can be added, removed, or changed after the list is created.
- **Duplicates are allowed:** A value can appear more than once.
- **Different data types are allowed:** A list can contain numbers, strings, and other types.
- **Indexed:** Each item can be accessed using its position.

Example:

```python
numbers = [2, 4, 4, 8]
print(numbers)
```

Output:

```text
[2, 4, 4, 8]
```

The duplicate value `4` is valid.

---

# 2. Creating and Printing a List

```python
marks = [1, 2, 3, 4, 5]
print(marks)
```

Output:

```text
[1, 2, 3, 4, 5]
```

- `marks` is the variable name.
- `[1, 2, 3, 4, 5]` is the list.
- `print()` displays the value on the screen.
- Square brackets and commas appear when Python prints a list directly.

A comment begins with `#`. Python ignores comments when running the program.

```python
# This is a comment. It explains the code but is not executed.
```

---

# 3. List Indexing

**Indexing** means accessing an item by its position. Python uses **zero-based indexing**, so the first item has index `0`, not `1`.

For this list:

```python
marks = [1, 2, 3, 4, 5]
```

| Value | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 |
| Negative index | -5 | -4 | -3 | -2 | -1 |

Examples:

```python
print(marks[0])   # 1: first item
print(marks[2])   # 3: third item
print(marks[4])   # 5: last item
print(marks[-1])  # 5: last item
print(marks[-2])  # 4: second-last item
```

### Adding values from a list

Your code uses:

```python
print(marks[0] + marks[4])
```

`marks[0]` is `1`, and `marks[4]` is `5`. Python adds them and prints `6`.

**Important:** Accessing an index that does not exist raises an `IndexError`. For example, `marks[5]` is invalid when the list has only five items.

---

# 4. Finding the Length of a List: `len()`

The built-in function `len()` returns the number of items in a list.

```python
marks = [1, 2, 3, 4, 5]
print(len(marks))
```

Output:

```text
5
```

The length is `5`, but the final positive index is `4`, because indexing starts from `0`.

**Remember:**

- Number of items = `len(marks)`
- Last positive index = `len(marks) - 1`

---

# 5. List Slicing

**Slicing** extracts a portion of a list without changing the original list.

General syntax:

```python
list_name[start:stop:step]
```

- `start`: index at which extraction begins; it is included.
- `stop`: index at which extraction ends; it is excluded.
- `step`: number of positions to move each time; it defaults to `1`.
- If `start` is omitted, slicing begins at the start of the list.
- If `stop` is omitted, slicing continues to the end of the list.

Start with:

```python
marks = [1, 2, 3, 4, 5]
```

### 5.1 `marks[1:4]`

```python
print(marks[1:4])
```

Output:

```text
[2, 3, 4]
```

It includes indexes `1`, `2`, and `3`. Index `4` is excluded.

### 5.2 `marks[1:]`

```python
print(marks[1:])
```

Output:

```text
[2, 3, 4, 5]
```

It starts at index `1` and continues to the end.

### 5.3 `marks[:4]`

```python
print(marks[:4])
```

Output:

```text
[1, 2, 3, 4]
```

It starts at the beginning and stops before index `4`.

### 5.4 `marks[-3:-1]`

```python
print(marks[-3:-1])
```

Output:

```text
[3, 4]
```

Negative indexes count from the right. Here, `-3` refers to `3`, while `-1` refers to `5`. Since the stop index is excluded, the result is `[3, 4]`.

### 5.5 More useful slicing examples

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:])     # [10, 20, 30, 40, 50]: a shallow copy
print(numbers[::2])   # [10, 30, 50]: every second item
print(numbers[::-1])  # [50, 40, 30, 20, 10]: reversed copy
```

**Key rule:** In ordinary slicing, the start is included and the stop is excluded.

---

# 6. Adding Items to a List

## 6.1 `append()`

`append()` adds one item to the end of the list.

```python
marks = [1, 2, 3, 4, 5]
marks.append(6)
print(marks)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

## 6.2 `insert()`

`insert()` adds an item at a particular index.

Syntax:

```python
list_name.insert(index, value)
```

Example:

```python
marks = [1, 2, 3, 4, 5, 6]
marks.insert(3, 9)
print(marks)
```

Output:

```text
[1, 2, 3, 9, 4, 5, 6]
```

The value `9` is inserted at index `3`. Existing items from that position onward shift to the right.

### Difference between `append()` and `insert()`

| Method | What it does | Example |
|---|---|---|
| `append(x)` | Adds `x` at the end | `marks.append(6)` |
| `insert(i, x)` | Adds `x` at index `i` | `marks.insert(3, 9)` |

Both methods modify the existing list.

---

# 7. Sorting and Reversing a List

## 7.1 `sort()`

`sort()` arranges list items in ascending order by default.

```python
numbers = [4, 1, 5, 2, 3]
numbers.sort()
print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

For numbers, ascending order means smallest to largest.

## 7.2 `sort(reverse=True)`

This sorts items in descending order.

```python
numbers.sort(reverse=True)
print(numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

Descending order means largest to smallest.

## 7.3 `reverse()`

`reverse()` reverses the current order of the items. It does **not** sort the list.

```python
numbers = [1, 3, 2, 5, 4]
numbers.reverse()
print(numbers)
```

Output:

```text
[4, 5, 2, 3, 1]
```

The original order was flipped exactly.

### Difference between `sort()` and `reverse()`

| Method | Purpose |
|---|---|
| `sort()` | Arranges items in ascending order |
| `sort(reverse=True)` | Arranges items in descending order |
| `reverse()` | Flips the current order without sorting |

**Important:** `sort()` and `reverse()` change the list directly and return `None`. Do not write `numbers = numbers.sort()` if you want to keep the sorted list; use `numbers.sort()` by itself.

---

# 8. Removing Items from a List

## 8.1 `remove()`

`remove(value)` removes the **first occurrence** of the given value.

```python
numbers = [1, 2, 9, 3, 9]
numbers.remove(9)
print(numbers)
```

Output:

```text
[1, 2, 3, 9]
```

Only the first `9` is removed. If the value does not exist, Python raises a `ValueError`.

## 8.2 `pop()`

`pop()` removes an item by its index and returns the removed item.

```python
numbers = [10, 20, 30, 40]
removed = numbers.pop(1)

print(removed)  # 20
print(numbers)  # [10, 30, 40]
```

If no index is supplied, `pop()` removes the last item.

```python
numbers = [10, 20, 30]
numbers.pop()
print(numbers)
```

Output:

```text
[10, 20]
```

### Difference between `remove()` and `pop()`

| Method | Removes by | Returns the removed item? |
|---|---|---|
| `remove(value)` | Value | No; returns `None` |
| `pop(index)` | Index | Yes |
| `pop()` | Last item by default | Yes |

Both `remove()` and `pop()` modify the original list.

---

# 9. Understanding the Complete List Practice Program

```python
# List practice
marks = [1, 2, 3, 4, 5]
print(marks)

print(marks[0] + marks[4])
print(len(marks))

# List slicing
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])

# Add an item at the end
marks.append(6)
print(marks)

# Insert 9 at index 3
marks.insert(3, 9)
print(marks)

# Sort from smallest to largest
marks.sort()
print(marks)

# Sort from largest to smallest
marks.sort(reverse=True)
print(marks)

# Reverse the current order
marks.reverse()
print(marks)

# Remove the value 9
marks.remove(9)
print(marks)

# Remove the item at index 4
marks.pop(4)
print(marks)
```

### Expected output

```text
[1, 2, 3, 4, 5]
6
5
[2, 3, 4]
[2, 3, 4, 5]
[1, 2, 3, 4]
[3, 4]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 9, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 9]
[9, 6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6, 9]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4]
```

### Why does the list change after each operation?

Python runs the statements from top to bottom. Each method that modifies the list affects the list used by the next statement.

1. The initial list is `[1, 2, 3, 4, 5]`.
2. `append(6)` produces `[1, 2, 3, 4, 5, 6]`.
3. `insert(3, 9)` produces `[1, 2, 3, 9, 4, 5, 6]`.
4. `sort()` produces `[1, 2, 3, 4, 5, 6, 9]`.
5. `sort(reverse=True)` produces `[9, 6, 5, 4, 3, 2, 1]`.
6. `reverse()` flips it to `[1, 2, 3, 4, 5, 6, 9]`.
7. `remove(9)` produces `[1, 2, 3, 4, 5, 6]`.
8. `pop(4)` removes the value `5`, producing `[1, 2, 3, 4, 6]`.

**Correction to note:** After `pop(4)`, the final list is `[1, 2, 3, 4, 6]`, because index `4` contains `6` only if the preceding state differs. In this program, after `remove(9)`, the list is `[1, 2, 3, 4, 5, 6]`; index `4` contains `5`, so the actual final list is `[1, 2, 3, 4, 6]`.

---

# 10. What Is a Palindrome?

A **palindrome** is a sequence that reads the same forwards and backwards.

Examples of palindromes:

- `121`
- `1331`
- `12321`
- `1 2 3 2 1` as a list of numbers

Examples that are not palindromes:

- `123`
- `1 2 3 4`
- `1 2 3 1`

A list is a palindrome if its sequence of elements is the same as its reverse.

For example:

```python
numbers = [1, 2, 3, 2, 1]
print(numbers == numbers[::-1])
```

Output:

```text
True
```

`numbers[::-1]` creates a reversed copy of the list. `==` checks whether the two lists contain equal items in the same order.

---

# 11. Understanding the Palindrome Program

Your code:

```python
print("ENTER number of ARRAY ELEMENTS")
n = int(input())

numbers = []
print("fill the array")

for i in range(n):
    numbers.append(int(input()))

numbers_copy = numbers.copy()

if numbers == numbers_copy[::-1]:
    print("it is palindrome")
else:
    print("not")
```

### Step-by-step explanation

**Step 1: Ask for the number of elements**

```python
n = int(input())
```

- `input()` reads text entered by the user.
- `int()` converts that text to an integer.
- `n` stores how many numbers the user wants to enter.

Example: if the user enters `5`, then `n = 5`.

**Step 2: Create an empty list**

```python
numbers = []
```

The list starts empty. The program will add the entered numbers to it.

**Step 3: Read the numbers using a loop**

```python
for i in range(n):
    numbers.append(int(input()))
```

- `range(n)` repeats the loop `n` times.
- `i` takes the values `0, 1, 2, ..., n-1`.
- `input()` reads one number each time.
- `int()` converts the entered text to an integer.
- `append()` adds the integer to the end of the list.

If `n = 5` and the inputs are `1`, `2`, `3`, `2`, `1`, the list becomes `[1, 2, 3, 2, 1]`.

**Step 4: Copy the list**

```python
numbers_copy = numbers.copy()
```

`copy()` creates a shallow copy of the list. For a list of integers, it gives a separate list containing the same values.

**Step 5: Reverse the copied list and compare**

```python
if numbers == numbers_copy[::-1]:
```

- `numbers_copy[::-1]` produces the elements in reverse order.
- `==` compares the original list with the reversed copy.
- If they are equal, the list is a palindrome.
- Otherwise, it is not a palindrome.

**Step 6: Print the result**

```python
if numbers == numbers_copy[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
```

### Example 1: Palindrome input

Input:

```text
5
1
2
3
2
1
```

Output:

```text
It is a palindrome
```

### Example 2: Not a palindrome

Input:

```text
4
1
2
3
4
```

Output:

```text
It is not a palindrome
```

### A simpler version

You do not need to copy the list to check it. Slicing already produces a reversed copy.

```python
numbers = [1, 2, 3, 2, 1]

if numbers == numbers[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
```

### Improve the input program with basic validation

This version rejects a negative number of elements. It assumes the user enters valid integers.

```python
n = int(input("Enter the number of array elements: "))

if n < 0:
    print("The number of elements cannot be negative.")
else:
    numbers = []

    for i in range(n):
        value = int(input(f"Enter element {i + 1}: "))
        numbers.append(value)

    if numbers == numbers[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
```

Note: An empty list is equal to its reverse, so this version treats `n = 0` as a palindrome. You can choose to handle an empty list differently if your assignment requires it.

---

# 12. Introduction to Tuples

A **tuple** is a Python data type that stores multiple items in an ordered collection, much like a list. Tuples are written using parentheses `()` in the usual case.

```python
tup = (1, 2, 3, 4)
print(tup)
print(type(tup))
print(tup[2])
```

Output:

```text
(1, 2, 3, 4)
<class 'tuple'>
3
```

### Explaining the code

- `tup = (1, 2, 3, 4)` creates a tuple.
- `print(tup)` displays its contents.
- `type(tup)` reports the data type.
- `tup[2]` accesses the element at index `2`, which is `3`.

As with lists, tuple indexing starts at `0`.

## 12.1 Main characteristics of tuples

- **Ordered:** Items keep their positions.
- **Immutable:** Items cannot be replaced, added, or removed after creation.
- **Duplicates are allowed:** Repeated values are valid.
- **Can contain different data types:** For example, `(10, "Python", True)`.
- **Supports indexing and slicing:** You can read individual elements or a portion of the tuple.

Example:

```python
tup = (10, 20, 30, 40)

print(tup[0])     # 10
print(tup[-1])    # 40
print(tup[1:3])   # (20, 30)
print(len(tup))   # 4
```

Trying to change an element causes an error:

```python
tup = (1, 2, 3)
# tup[0] = 10  # TypeError: tuples do not support item assignment
```

## 12.2 A tuple with one element

A comma is required to create a one-element tuple.

```python
single = (5,)
print(type(single))  # <class 'tuple'>

not_a_tuple = (5)
print(type(not_a_tuple))  # <class 'int'>
```

Parentheses alone do not make a tuple; the comma does.

## 12.3 List vs tuple

| Feature | List | Tuple |
|---|---|---|
| Brackets commonly used | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates allowed | Yes | Yes |
| Indexing and slicing | Yes | Yes |
| Can be modified after creation | Yes | No |

**When should you use each?**

- Use a **list** when the collection needs to change, such as a list of bookings or scores.
- Use a **tuple** when the collection should remain fixed, such as a fixed coordinate or RGB colour values.

---

# 13. Common Errors and Important Points

1. **Index out of range:** Accessing `numbers[5]` when a list has only five elements causes an `IndexError`.
2. **Stop index in slicing is excluded:** `numbers[1:4]` does not include index `4`.
3. **`append()` adds one item:** `numbers.append([6, 7])` adds a nested list as one item, not two separate integers.
4. **`remove()` uses a value:** `numbers.remove(3)` removes the first matching value `3`.
5. **`pop()` uses an index:** `numbers.pop(3)` removes the item at index `3`.
6. **`sort()` changes the list:** It sorts in place and returns `None`.
7. **`reverse()` does not sort:** It only flips the existing order.
8. **`input()` returns a string:** Use `int(input())` when an integer is needed.
9. **Use clear variable names:** Avoid naming a list `list`, because `list` is also a Python built-in type. Prefer names such as `numbers`, `marks`, or `values`.
10. **Indentation matters:** The statements inside a `for` loop or an `if`/`else` block must be indented consistently.

---

# 14. Quick Revision Sheet

| Concept | Meaning / Example |
|---|---|
| Create a list | `numbers = [1, 2, 3]` |
| Access first item | `numbers[0]` |
| Access last item | `numbers[-1]` |
| Find number of items | `len(numbers)` |
| Slice a list | `numbers[1:3]` |
| Reverse a copy | `numbers[::-1]` |
| Add at the end | `numbers.append(4)` |
| Insert at an index | `numbers.insert(1, 9)` |
| Sort ascending | `numbers.sort()` |
| Sort descending | `numbers.sort(reverse=True)` |
| Reverse in place | `numbers.reverse()` |
| Remove by value | `numbers.remove(2)` |
| Remove by index | `numbers.pop(1)` |
| Copy a list | `numbers.copy()` |
| Compare lists | `numbers == other_numbers` |
| Create a tuple | `tup = (1, 2, 3)` |
| Find the data type | `type(tup)` |
| Access a tuple item | `tup[2]` |

---

# 15. Practice Questions

Try answering these questions before checking your code.

1. Create a list of five numbers and print the third item.
2. Find the length of a list using `len()`.
3. Print the first three elements using slicing.
4. Print the last two elements using negative indexes.
5. Add a value using `append()` and insert another value using `insert()`.
6. Sort a list in ascending and descending order.
7. Explain the difference between `reverse()` and `sort(reverse=True)`.
8. Remove a value using `remove()` and an item using `pop()`.
9. Write a program to check whether a list of integers is a palindrome.
10. Create a tuple, print its type, and access its second element.
11. Explain why `tup = (5,)` is a tuple but `tup = (5)` is an integer.
12. Explain the difference between a list and a tuple.

## Final learning checklist

After studying these notes, you should be able to:

- [ ] Explain what a list is and describe its main properties.
- [ ] Use positive and negative indexing.
- [ ] Find the length of a list.
- [ ] Understand slicing and its start/stop rules.
- [ ] Add, sort, reverse, and remove list elements.
- [ ] Trace a program and predict how a list changes line by line.
- [ ] Use loops and `input()` to build a list from user input.
- [ ] Check whether a list is a palindrome.
- [ ] Create tuples, access their elements, and explain immutability.
- [ ] Distinguish between lists and tuples.

**Suggested GitHub location:** `Notes/03_Lists_Palindromes_Tuples.md`

**Suggested code location:** `Codes/list_practice.py`
