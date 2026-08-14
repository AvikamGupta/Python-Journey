# 🐍 Python Journey — Day 2

> **Topics Covered:** Strings, Escape Characters, Concatenation, `len()`, Indexing, Slicing, String Functions, `if-elif-else`

---

## 📌 1. Strings

A **string** is a sequence of characters enclosed inside:

* Double quotes `" "`
* Single quotes `' '`
* Triple quotes `""" """`

### Example

```python
str1 = "this is a string"
str2 = 'VIT'
str3 = """this is a string but in triple quotes"""

print(str1)
print(str2)
print(str3)
```

### 💡 Remember

All of these are valid strings:

```python
"Hello"
'Hello'
"""Hello"""
```

---

## 📌 2. Escape Characters

Escape characters are used to represent special characters inside strings.

### `\n` → New Line

```python
str4 = "this is a string \n in python"
print(str4)
```

**Output:**

```text
this is a string
 in python
```

### Common Escape Characters

| Escape Character | Meaning      |
| ---------------- | ------------ |
| `\n`             | New line     |
| `\t`             | Tab space    |
| `\\`             | Backslash    |
| `\"`             | Double quote |
| `\'`             | Single quote |

---

## 📌 3. String Concatenation

**Concatenation** means joining two or more strings together.

The `+` operator is used for concatenation.

```python
str1 = "this is a string"
str2 = "VIT"

print(str1 + str2)
```

**Output:**

```text
this is a stringVIT
```

### 💡 Adding a space

```python
print(str1 + " " + str2)
```

**Output:**

```text
this is a string VIT
```

---

# 📌 4. `len()` Function

The `len()` function returns the **number of characters** in a string.

Spaces are also counted as characters.

```python
str1 = "this is a string"
str2 = "VIT"
str3 = """this is a string but in triple quotes"""

print(len(str1))
print(len(str2))
print(len(str3))
```

### 💡 Important

```python
len("VIT")
```

Output:

```text
3
```

Because:

```text
V → 1
I → 2
T → 3
```

---

# 📌 5. String Indexing

**Indexing** means accessing individual characters of a string.

> ⚠️ Python indexing starts from **0**.

For:

```python
str2 = "VIT"
```

The indexes are:

```text
Character:  V   I   T
Index:      0   1   2
```

### Example

```python
print(str2[1])
```

**Output:**

```text
I
```

### 💡 Remember

```text
First character  → index 0
Second character → index 1
Third character  → index 2
```

---

# 📌 6. String Slicing

**Slicing** is used to extract a portion of a string.

### Syntax

```python
string[start:end]
```

> ⚠️ The **ending index is not included**.

### Example

```python
str3 = "this is a string but in triple quotes"

print(str3[3:7])
```

Python takes characters from:

```text
index 3 → index 6
```

Index `7` is **not included**.

---

## 🔹 Slicing from an Index to the End

```python
print(str3[3:len(str3)])
```

This starts from index `3` and goes until the end.

### Shortcut

Instead of:

```python
print(str3[3:len(str3)])
```

You can write:

```python
print(str3[3:])
```

Python automatically understands that the missing ending index means:

> **Go until the end of the string.**

---

## 🔹 Slicing from the Beginning

```python
print(str3[:7])
```

This means:

```text
Start from index 0 → Stop before index 7
```

---

# 📌 7. Negative Indexing

Python also supports **negative indexing**.

Negative indexing starts from the end of the string.

```python
str2 = "VIT"
```

The indexes are:

```text
Character:   V    I    T
Positive:    0    1    2
Negative:   -3   -2   -1
```

### Example

```python
print(str2[-3:-1])
```

The ending index `-1` is not included.

So the output is:

```text
VI
```

### 💡 Remember

The last character always has index:

```text
-1
```

---

# 📌 8. String Functions

Python provides several built-in string methods/functions.

Let's use:

```python
str5 = "i am studying python from apna college"
```

---

## 🔹 `endswith()`

Checks whether a string ends with a particular value.

```python
print(str5.endswith("ege"))
```

Output:

```text
True
```

### Example

```python
print(str5.endswith("college"))
```

Output:

```text
True
```

---

## 🔹 `capitalize()`

Capitalizes the **first character** of the string.

```python
print(str5.capitalize())
```

Output:

```text
I am studying python from apna college
```

### 💡 Important

`capitalize()` does **not** capitalize every word.

---

## 🔹 `replace()`

Replaces one value with another.

### Syntax

```python
string.replace(old, new)
```

### Example

```python
print(str5.replace("o", "a"))
```

This replaces every occurrence of `"o"` with `"a"`.

---

## 🔹 `find()`

Returns the index of the **first occurrence** of a value.

```python
print(str5.find("o"))
```

If the value is not found, `find()` returns:

```text
-1
```

### Example

```python
print(str5.find("python"))
```

This returns the index where `"python"` starts.

---

## 🔹 `count()`

Returns the number of times a value occurs in a string.

```python
print(str5.count("am"))
```

If the value does not exist, it returns:

```text
0
```

### 💡 Important Correction

`count()` returns `0` when the substring is not found.

`find()` returns `-1` when the substring is not found.

---

# 🧠 String Functions Quick Revision

| Function       | Purpose                      |
| -------------- | ---------------------------- |
| `len()`        | Returns number of characters |
| `endswith()`   | Checks ending of string      |
| `capitalize()` | Capitalizes first character  |
| `replace()`    | Replaces values              |
| `find()`       | Finds first occurrence       |
| `count()`      | Counts occurrences           |

---

# 📌 9. `if-elif-else`

Conditional statements are used to make decisions in Python.

### Basic Structure

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

### 💡 Important Rules

1. Use a **colon `:`** after `if`, `elif`, and `else`.
2. Python uses **indentation** to define blocks.
3. Usually, **4 spaces** are used for indentation.

---

# 🚦 10. Traffic Light Example

```python
color = input("What is the colour of the traffic light: ")

if color == "red":
    print("Stop")

elif color == "yellow":
    print("Be ready to move")

else:
    print("Move")
```

### How it works

If the user enters:

```text
red
```

Output:

```text
Stop
```

If the user enters:

```text
yellow
```

Output:

```text
Be ready to move
```

For any other input:

```text
Move
```

---

# 📌 11. Comparison Operator

In conditions, we use:

```python
==
```

to check whether two values are equal.

### Example

```python
color == "red"
```

This asks:

> Is the value of `color` equal to `"red"`?

### ⚠️ Important

Do not confuse:

```python
=
```

with:

```python
==
```

| Operator | Meaning    |
| -------- | ---------- |
| `=`      | Assignment |
| `==`     | Comparison |

Example:

```python
age = 18
```

means:

> Store `18` in `age`.

While:

```python
age == 18
```

means:

> Check whether `age` is equal to `18`.

---

# 🧩 12. Complete Day 2 Code

```python
# Strings
str1 = "this is a string"
str2 = "VIT"
str3 = """this is a string but in triple quotes"""

# Escape characters
str4 = "this is a string \n in python"
print(str4)

# Concatenation
print(str1 + str2)

# Length
print(len(str1))
print(len(str2))
print(len(str3))

# Indexing
print(str2[1])

# Slicing
print(str3[3:7])
print(str3[3:len(str3)])
print(str3[2:])

# Negative indexing
print(str2[-3:-1])

# String functions
str5 = "i am studying python from apna college"

print(str5.endswith("ege"))
print(str5.capitalize())
print(str5.replace("o", "a"))
print(str5.find("o"))
print(str5.count("am"))

# If-elif-else
color = input("What is the colour of the traffic light: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Be ready to move")
else:
    print("Move")
```

---

# ⚡ Day 2 Quick Revision

### Strings

```python
str = "Python"
```

### Length

```python
len(str)
```

### Indexing

```python
str[0]
```

### Slicing

```python
str[1:4]
```

### Negative Indexing

```python
str[-1]
```

### Concatenation

```python
str1 + str2
```

### String Methods

```python
str.endswith()
str.capitalize()
str.replace()
str.find()
str.count()
```

### Conditions

```python
if condition:
    statement
elif condition:
    statement
else:
    statement
```

---

# 🎯 Day 2 Practice

Try solving these **without looking at the answers**.

### 🟢 Beginner

* [ ] Create a string containing your name and print its length.
* [ ] Print the first character of your name using indexing.
* [ ] Print the last character using negative indexing.
* [ ] Create two strings and concatenate them.
* [ ] Check whether your name ends with a particular character.

### 🟡 Intermediate

* [ ] Take a string as input and print its first 3 characters.
* [ ] Take a string as input and print it in reverse using slicing.
* [ ] Count how many times `"a"` appears in a string.
* [ ] Replace all spaces in a string with `"-"`.
* [ ] Find the first occurrence of a particular character.

### 🔴 Challenge

Create a traffic-light program that:

```text
red    → Stop
yellow → Get Ready
green  → Go
```

Also handle unexpected input using `else`.

---

# 🧠 Key Takeaways

> **Day 2 = Strings + Conditions**

Remember these core concepts:

```text
Strings
   ↓
Escape Characters
   ↓
Concatenation
   ↓
len()
   ↓
Indexing
   ↓
Slicing
   ↓
Negative Indexing
   ↓
String Methods
   ↓
if-elif-else
```

### ⭐ Most Important Rules

```text
Indexing starts from 0
Slicing excludes the ending index
Last negative index is -1
len() counts spaces
=  means assignment
== means comparison
if/elif/else require :
Indentation defines code blocks
```

---

## 🚀 Day 2 Status

**Topics Completed:** ✅

* [x] Strings
* [x] Escape Characters
* [x] Concatenation
* [x] `len()`
* [x] Indexing
* [x] Slicing
* [x] Negative Indexing
* [x] String Methods
* [x] `if-elif-else`

**Next Step:** 🐍 Continue to the next Python topic.
