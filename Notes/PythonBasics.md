# Python Basics — Variables, Data Types, Operators & Input

## 1. Printing in Python

The `print()` function is used to display output on the screen.

```python
print("my name is Avikam")
print("i am learning basic programming of Python")
```

### Printing multiple values

Multiple values can be passed to `print()` by separating them with commas.

```python
print("I am learning", "Python")
```

Python automatically adds a space between the values.

---

## 2. Variables

A variable is a name used to store a value in memory.

```python
name = "Avikam"
age = 18
```

Here:

* `name` stores the string `"Avikam"`
* `age` stores the integer `18`

Variables can be used later in the program:

```python
print("My name is:", name)
print("My age is:", age)
```

### Important

Python is **dynamically typed**, which means we do not need to explicitly declare the data type of a variable.

```python
age = 18
name = "Avikam"
```

Python automatically determines their types.

---

## 3. Comments

Comments are ignored by Python and are mainly used to explain code.

### Single-line comment

Use `#` for a single-line comment.

```python
# This is a comment
age = 18
```

### Multi-line strings

Triple quotes can be used to create multi-line strings.

```python
"""
This is a multi-line string.
It can span multiple lines.
"""
```

> **Note:** Triple-quoted strings are technically strings, not comments. They are often used like comments when they are not assigned to a variable.

---

# 4. Basic Arithmetic Operators

Python supports common mathematical operations.

```python
a = 5
b = 2
```

### Multiplication

```python
result = a * b
print(result)
```

Output:

```text
10
```

### Exponentiation

The `**` operator is used for power.

```python
print(a ** b)
```

Since:

```text
5² = 25
```

Output:

```text
25
```

### Common Arithmetic Operators

| Operator | Meaning             | Example  | Result |
| -------- | ------------------- | -------- | -----: |
| `+`      | Addition            | `5 + 2`  |    `7` |
| `-`      | Subtraction         | `5 - 2`  |    `3` |
| `*`      | Multiplication      | `5 * 2`  |   `10` |
| `/`      | Division            | `5 / 2`  |  `2.5` |
| `//`     | Floor Division      | `5 // 2` |    `2` |
| `%`      | Modulus / Remainder | `5 % 2`  |    `1` |
| `**`     | Exponentiation      | `5 ** 2` |   `25` |

---

# 5. Comparison Operators

Comparison operators compare two values and return either:

* `True`
* `False`

Example:

```python
a = 5
b = 2

print(a > b)
```

Output:

```text
True
```

Because `5` is greater than `2`.

### Common Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |

Example:

```python
print(a > b)
print(b > a)
print(a == b)
print(a != b)
```

---

# 6. Logical Operators

Logical operators are used to combine or modify conditions.

Python has three main logical operators:

* `and`
* `or`
* `not`

## `and`

Returns `True` only when **both conditions are True**.

```python
print((a > b) and (b == a))
```

Here:

```text
a > b  → True
b == a → False
```

Therefore:

```text
True and False → False
```

---

## `or`

Returns `True` if **at least one condition is True**.

```python
print((a > b) or (b == a))
```

Here:

```text
True or False → True
```

---

## `not`

`not` reverses the Boolean value.

```python
print(not (a > b))
```

Since:

```text
a > b → True
```

`not` changes it to:

```text
False
```

### Quick Summary

| Operator | Description                            |
| -------- | -------------------------------------- |
| `and`    | True only if both conditions are True  |
| `or`     | True if at least one condition is True |
| `not`    | Reverses True/False                    |

---

# 7. Data Types

A data type tells Python what kind of value a variable contains.

Some basic Python data types are:

* `int` → Integer
* `float` → Decimal number
* `str` → String
* `bool` → Boolean

Examples:

```python
age = 18          # int
percentage = 87.5 # float
name = "Avikam"   # str
passed = True     # bool
```

---

# 8. `type()` Function

The `type()` function tells us the data type of a value or variable.

```python
name = "Avikam"
age = 18

print(type(name))
print(type(age))
```

Output:

```text
<class 'str'>
<class 'int'>
```

Example:

```python
a = 2.4
print(type(a))
```

Output:

```text
<class 'float'>
```

---

# 9. Type Conversion / Type Casting

Type conversion means converting a value from one data type to another.

Common conversion functions:

```python
int()
float()
str()
bool()
```

### String to Integer

```python
b = int("3")
print(b)
```

The string `"3"` is converted into the integer `3`.

```python
print(type(b))
```

Output:

```text
<class 'int'>
```

### Important

The string must contain a valid numeric value.

This works:

```python
int("3")
```

This does not work:

```python
int("Avikam")
```

because `"Avikam"` cannot be converted into an integer.

### Float to Integer

```python
x = int(2.9)
print(x)
```

Output:

```text
2
```

The decimal part is removed.

---

# 10. Taking Input from the User

Python uses the `input()` function to take input from the user.

```python
name = input("Enter your name: ")
```

The user enters something, and Python stores it in `name`.

### Important Rule

**`input()` always returns a string.**

For example:

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
18
```

Python initially stores it as:

```python
"18"
```

which is a string.

---

# 11. Taking Integer Input

If we want an integer, we need to convert the input.

```python
age = int(input("Enter your age: "))
```

The process is:

```text
input()
   ↓
string
   ↓
int()
   ↓
integer
```

---

# 12. Taking Float Input

For decimal values, use `float()`.

```python
percentile = float(input("Enter your percentile: "))
```

For example, if the user enters:

```text
72.31
```

the value is stored as a `float`.

---

# 13. Complete Input Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentile = float(input("Enter your percentile: "))

print("Welcome", name)
print("Age =", age)
print("Percentile =", percentile)
```

Example interaction:

```text
Enter your name: Avikam
Enter your age: 18
Enter your percentile: 72.31

Welcome Avikam
Age = 18
Percentile = 72.31
```

---

# 14. Key Takeaways

* `print()` is used to display output.
* Variables store values.
* Python is dynamically typed.
* `#` is used for single-line comments.
* `**` is used for exponentiation.
* Comparison operators return `True` or `False`.
* `and`, `or`, and `not` are logical operators.
* `type()` tells us the type of a value.
* `int()`, `float()`, `str()`, and `bool()` are commonly used for type conversion.
* `input()` always returns a string.
* Convert user input when a number is required.

## Core Concepts Covered

```text
Python Basics
│
├── print()
├── Variables
├── Comments
├── Arithmetic Operators
├── Comparison Operators
├── Logical Operators
├── Data Types
├── type()
├── Type Conversion
└── input()
```
