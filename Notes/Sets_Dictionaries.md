# Python Dictionaries and Sets — Complete Beginner-Friendly Notes

**Purpose:** These notes explain the dictionary and set concepts used in the practice code. They include definitions, syntax, examples, expected outputs, common errors, and practice questions.

**Suggested GitHub location:** `Notes/04_Dictionaries_and_Sets.md`  
**Suggested code location:** `Codes/dictionary_set_practice.py`

---

# Part 1: Python Dictionaries

## 1. What Is a Dictionary?

A **dictionary** is a Python data type that stores information as **key–value pairs**. Each key is used to access its corresponding value.

Dictionaries are written using curly braces `{}`.

```python
student = {
    "name": "Avikam",
    "age": 18,
    "cgpa": 9.6
}
```

In this example:

- `"name"`, `"age"`, and `"cgpa"` are **keys**.
- `"Avikam"`, `18`, and `9.6` are their corresponding **values**.
- Each key is associated with one value.

To access a value, use its key:

```python
print(student["name"])  # Avikam
print(student["age"])   # 18
```

## 2. Main Characteristics of Dictionaries

- **Key–value structure:** Each entry contains a key and a value.
- **Mutable:** You can add, update, or remove entries.
- **Keys are unique:** If a key is repeated, its later value replaces the earlier value.
- **Keys must be hashable:** Common examples include strings, integers, and tuples containing only hashable values. Lists and dictionaries cannot be used as dictionary keys.
- **Values can be different data types:** Values can be strings, numbers, Boolean values, lists, or even other dictionaries.
- **Insertion order is preserved:** Modern Python dictionaries preserve the order in which entries are inserted.
- **Accessed by key:** Use the key or a method such as `items()` rather than list-style numerical indexing.

Example of a repeated key:

```python
example = {"age": 18, "age": 19}
print(example)
# {'age': 19}
```

The second value replaces the first one.

---

## 3. Creating a Nested Dictionary

Your code stores several kinds of information in one dictionary, including another dictionary and a list.

```python
info = {
    "name": "avikam",
    "student": {
        "phy": 99,
        "chem": 98,
        "maths": 100
    },
    "age": 18,
    "learning": ["java", "python", "cpp"],
    "is_adult": True,
    "cgpa": 9.6
}
```

### Understanding each entry

| Key | Value | Data type |
|---|---|---|
| `"name"` | `"avikam"` | String |
| `"student"` | `{"phy": 99, "chem": 98, "maths": 100}` | Dictionary |
| `"age"` | `18` | Integer |
| `"learning"` | `["java", "python", "cpp"]` | List |
| `"is_adult"` | `True` | Boolean |
| `"cgpa"` | `9.6` | Float |

The `"student"` key contains a **nested dictionary**—a dictionary inside another dictionary.

The `"learning"` key contains a **list** inside the dictionary.

Dictionaries can combine different data structures to represent related information clearly.

---

## 4. Printing a Dictionary

```python
print(info)
```

This displays the complete dictionary, including all its keys and values.

Python may display strings with single quotes even if you originally used double quotes. Both are valid ways to write string literals.

---

## 5. Accessing Dictionary Values

Use square brackets with a key:

```python
print(info["name"])
print(info["learning"])
print(info["student"]["maths"])
```

Output:

```text
avikam
['java', 'python', 'cpp']
100
```

### Explanation

- `info["name"]` gets the value associated with `"name"`.
- `info["learning"]` gets the list stored under `"learning"`.
- `info["student"]["maths"]` first accesses the nested dictionary under `"student"`, then gets its `"maths"` value.

### Accessing a list stored inside a dictionary

```python
print(info["learning"][0])  # java
print(info["learning"][1])  # python
```

The first pair of brackets accesses the dictionary key. The second pair accesses a list index.

### What if a key does not exist?

Using `info["city"]` before `"city"` has been added raises a `KeyError`.

Use `get()` when you want a safer lookup:

```python
print(info.get("city"))              # None
print(info.get("city", "Not found")) # Not found
```

`get(key, default)` returns the default value if the key is missing. It does not automatically add that key to the dictionary.

---

## 6. Dictionary Methods

A **method** is an operation associated with a particular object, such as a dictionary.

### 6.1 `keys()`

Returns a view of all the dictionary's keys.

```python
print(info.keys())
```

Typical output begins like this:

```text
dict_keys(['name', 'student', 'age', 'learning', 'is_adult', 'cgpa'])
```

### 6.2 `values()`

Returns a view of all the values.

```python
print(info.values())
```

The output includes the name, nested dictionary, age, learning list, Boolean value, and CGPA.

### 6.3 `items()`

Returns a view of the dictionary's key–value pairs. Each pair behaves like a two-item tuple.

```python
print(info.items())
```

Typical output begins like this:

```text
dict_items([('name', 'avikam'), ('student', {'phy': 99, 'chem': 98, 'maths': 100}), ...])
```

### Quick comparison

| Method | Returns | Typical use |
|---|---|---|
| `keys()` | All keys | See or loop through keys |
| `values()` | All values | See or loop through values |
| `items()` | Key–value pairs | Process both key and value |
| `get(key)` | One value, or `None` if absent | Safely look up a key |

These methods return **view objects**, not ordinary lists. Convert a view to a list if needed:

```python
print(list(info.keys()))
print(list(info.values()))
print(list(info.items()))
```

Here, `list()` is a built-in conversion function.

---

## 7. Updating a Dictionary

Dictionaries are mutable, so values can be changed and new entries can be added.

### 7.1 Updating an existing value

```python
info.update({"age": 19})
print(info["age"])
```

Output:

```text
19
```

Because `"age"` already exists, its value changes from `18` to `19`.

You can also assign directly:

```python
info["age"] = 19
```

### 7.2 Adding a new key–value pair with `update()`

```python
new_dict = {"city": "Kanpur"}
info.update(new_dict)
print(info["city"])
```

Output:

```text
Kanpur
```

Since `"city"` was not present, it is added to `info`.

### 7.3 Updating more than one entry

```python
info.update({
    "age": 20,
    "city": "Bhopal"
})
```

This updates the age and adds or replaces the city value.

### Important distinction

- If the key exists, `update()` replaces its value.
- If the key does not exist, `update()` adds it.
- `update()` modifies the original dictionary; it does not create a new dictionary.

---

## 8. Looping Through a Dictionary

A `for` loop can process dictionary entries.

```python
for key in info:
    print(key)
```

This prints each key.

To print each value:

```python
for value in info.values():
    print(value)
```

To print both keys and values:

```python
for key, value in info.items():
    print(key, ":", value)
```

`key, value` unpack each key–value pair returned by `items()`.

---

## 9. Removing Dictionary Entries

These are useful basic dictionary operations.

### `pop(key)`

Removes a key and returns its value.

```python
student = {"name": "Avikam", "age": 18}
age = student.pop("age")
print(age)      # 18
print(student)  # {'name': 'Avikam'}
```

If the key is missing and no default is provided, `pop()` raises `KeyError`.

### `del`

Deletes a particular entry.

```python
student = {"name": "Avikam", "age": 18}
del student["age"]
print(student)  # {'name': 'Avikam'}
```

### `clear()`

Removes all entries.

```python
student.clear()
print(student)  # {}
```

---

# Part 2: Python Sets

## 10. What Is a Set?

A **set** is a collection of **unique items**. Sets are written using curly braces `{}` when they contain elements.

```python
nums = {1, 2, 3, 4}
print(nums)
```

Sets are useful when you need to remove duplicates or perform mathematical set operations.

## 11. Main Characteristics of Sets

- **Unique elements:** Duplicate values are stored only once.
- **Mutable:** Items can be added or removed.
- **Unordered:** Sets do not guarantee a particular display or iteration order. Do not rely on the order in which values are printed.
- **No indexing or slicing:** You cannot use `nums[0]` or `nums[1:3]`.
- **Elements must be hashable:** Integers, strings, and many tuples are valid elements. Lists and dictionaries are not valid set elements.
- **Can contain different types:** Provided the elements are hashable.

---

## 12. Creating a Set and Removing Duplicates

Your code:

```python
nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}

print(set2)
```

Output:

```text
{1, 2}
```

Although `2` appears three times in the source, a set stores each distinct value only once.

This makes sets useful for finding unique values in a collection.

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
```

The set contains only `1`, `2`, `3`, and `4`. Its displayed order is not guaranteed.

**Note:** Converting a list to a set removes duplicates, but it does not preserve the list's positional order as a set guarantee.

---

## 13. Creating an Empty Set

This is an important Python rule.

```python
empty_set = set()
```

This creates an empty set.

Do **not** use `{}` to create an empty set:

```python
empty = {}
print(type(empty))
```

Output:

```text
<class 'dict'>
```

An empty pair of curly braces creates an empty **dictionary**, not a set.

Remember:

- `{1, 2, 3}` creates a set.
- `set()` creates an empty set.
- `{}` creates an empty dictionary.

---

## 14. Adding Elements to a Set: `add()`

The `add()` method adds one element to a set.

```python
nums = {1, 2, 3, 4}
nums.add(5)
print(nums)
```

The set now contains `1`, `2`, `3`, `4`, and `5`.

Adding a value that is already present does not create a duplicate:

```python
nums.add(5)
print(nums)
```

The set still contains only one `5`.

### `add()` vs `update()`

`add()` adds one element. `update()` can add multiple elements from an iterable.

```python
nums = {1, 2}
nums.add(3)
nums.update([4, 5, 6])

print(nums)
```

The set contains the unique values `1` through `6`; its display order is not guaranteed.

---

## 15. Removing Elements from a Set

Your last line is:

```python
set.remove()
```

This line is incomplete and will cause a `TypeError`, because `remove()` requires the value to remove. Also, the variable you created is named `nums`, not `set`.

Correct example:

```python
nums = {1, 2, 3, 4}
nums.remove(3)
print(nums)
```

The set now contains `1`, `2`, and `4`.

### `remove()` vs `discard()`

```python
nums = {1, 2, 3}

nums.remove(2)   # Removes 2
nums.discard(10) # Does nothing if 10 is absent
```

- `remove(value)` raises a `KeyError` if the value is not present.
- `discard(value)` does not raise an error if the value is absent.

### `pop()`

`pop()` removes and returns an arbitrary element from a set. Since sets are unordered, do not assume which item will be removed.

```python
nums = {10, 20, 30}
removed = nums.pop()

print(removed)
print(nums)
```

The exact removed element is not guaranteed.

### `clear()`

Removes all elements from a set.

```python
nums = {1, 2, 3}
nums.clear()
print(nums)  # set()
```

An empty set displays as `set()`, not `{}`.

---

## 16. Mathematical Set Operations

Suppose:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

### 16.1 Union: `|` or `union()`

Union combines all distinct elements from both sets.

```python
print(A | B)
print(A.union(B))
```

Result: a set containing `1`, `2`, `3`, `4`, and `5`. The display order is not guaranteed.

### 16.2 Intersection: `&` or `intersection()`

Intersection contains elements common to both sets.

```python
print(A & B)
print(A.intersection(B))
```

Result: `{3}`.

### 16.3 Difference: `-` or `difference()`

Difference contains elements in the first set that are not in the second.

```python
print(A - B)  # {1, 2}
print(B - A)  # {4, 5}
```

Set difference is directional: `A - B` is not necessarily the same as `B - A`.

### 16.4 Symmetric difference: `^`

Returns elements that belong to either set, but not both.

```python
print(A ^ B)
```

Result: a set containing `1`, `2`, `4`, and `5`.

### 16.5 Subset and superset

```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
```

A is a subset of B because every element of A is also in B.

---

# Part 3: Understanding and Correcting Your Original Code

## 17. Dictionary Program

Your dictionary code, with comments and clearer formatting:

```python
# Dictionary practice

info = {
    "name": "avikam",
    "student": {
        "phy": 99,
        "chem": 98,
        "maths": 100
    },
    "age": 18,
    "learning": ["java", "python", "cpp"],
    "is_adult": True,
    "cgpa": 9.6
}

# Print the complete dictionary
print(info)

# Access values by key
print(info["name"])
print(info["learning"])

# Access a value inside the nested dictionary
print(info["student"]["maths"])

# View keys, values, and key-value pairs
print(info.keys())
print(info.values())
print(info.items())

# Update an existing value
info.update({"age": 19})

# Add a new key-value pair
new_dict = {"city": "Kanpur"}
info.update(new_dict)

print(info)
```

The final dictionary has `"age": 19` and `"city": "Kanpur"`. The original `"student"`, `"learning"`, and other entries remain unchanged.

## 18. Corrected Set Program

```python
# Set practice

nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}

# Create an empty set
null_set = set()

print(nums)
print(set2)       # Duplicates are removed
print(null_set)   # set()

# Add an element
nums.add(5)
print(nums)

# Remove an element that exists
nums.remove(3)
print(nums)

# Safely attempt to remove a possibly absent element
nums.discard(10)
print(nums)
```

**Important correction:** `set.remove()` is not valid without an argument. Use `nums.remove(value)` to remove a value from the set named `nums`.

---

# Part 4: Dictionary vs Set

Both dictionaries and sets use curly braces in many situations, but they serve different purposes.

| Feature | Dictionary | Set |
|---|---|---|
| Stores | Key–value pairs | Unique elements |
| Example | `{"name": "Avikam"}` | `{"Java", "Python"}` |
| Duplicate keys/elements | Keys are unique | Elements are unique |
| Access | By key | No indexing; test membership or iterate |
| Mutable | Yes | Yes |
| Empty form | `{}` | `set()` |
| Common uses | Profiles, marks, settings | Unique values, membership checks, set mathematics |

### A quick way to remember

- **List:** Ordered collection that can contain duplicates and be changed.
- **Tuple:** Ordered collection that cannot be changed.
- **Dictionary:** Maps keys to values.
- **Set:** Stores unique elements without guaranteeing order.

---

# Part 5: Common Errors to Avoid

1. **Using a missing dictionary key:** `info["city"]` raises `KeyError` if `"city"` is absent. Use `get()` when appropriate.
2. **Confusing keys and values:** `info.keys()` returns keys; `info.values()` returns values.
3. **Forgetting nested access:** Use `info["student"]["maths"]` to reach a nested value.
4. **Assuming dictionary methods return lists:** `keys()`, `values()`, and `items()` return view objects; use `list(...)` if a list is needed.
5. **Expecting duplicate set elements:** `{1, 2, 2, 3}` stores each distinct value once.
6. **Creating an empty set with `{}`:** This creates an empty dictionary. Use `set()`.
7. **Using a set index:** `nums[0]` is invalid because sets do not support indexing.
8. **Calling `remove()` without a value:** `nums.remove(3)` is valid; `nums.remove()` is not.
9. **Removing an absent set element:** `remove()` raises `KeyError`; `discard()` does not.
10. **Assuming a set has a fixed display order:** Set order is not guaranteed.

---

# Part 6: Quick Revision Sheet

| Operation | Example | Purpose |
|---|---|---|
| Create dictionary | `info = {"age": 18}` | Store key–value pairs |
| Access value | `info["age"]` | Retrieve a value by key |
| Safe lookup | `info.get("city", "Unknown")` | Provide a default for a missing key |
| Get keys | `info.keys()` | Inspect keys |
| Get values | `info.values()` | Inspect values |
| Get pairs | `info.items()` | Inspect key–value pairs |
| Add/update | `info.update({"age": 19})` | Add or replace entries |
| Remove dictionary key | `info.pop("age")` | Remove and return a value |
| Create set | `nums = {1, 2, 3}` | Store unique elements |
| Create empty set | `nums = set()` | Create an empty set |
| Add one item | `nums.add(4)` | Add an element |
| Add multiple items | `nums.update([4, 5])` | Add multiple elements |
| Remove an item | `nums.remove(2)` | Remove; error if absent |
| Safe removal | `nums.discard(2)` | No error if absent |
| Union | `A \| B` | Combine unique elements |
| Intersection | `A & B` | Find common elements |
| Difference | `A - B` | Find elements only in A |
| Symmetric difference | `A ^ B` | Find elements in either, but not both |

---

# Part 7: Practice Questions

Try these before looking up solutions.

## Dictionary practice

1. Create a dictionary with your name, age, and favourite programming language.
2. Print one value using its key.
3. Add a `"city"` key.
4. Update the age.
5. Print all keys and all values.
6. Use `items()` to print each key and value on a separate line.
7. Create a nested dictionary containing marks for three subjects and print the maths mark.
8. Explain the difference between `info["city"]` and `info.get("city")`.

## Set practice

1. Create a set containing repeated numbers and observe what is printed.
2. Create an empty set correctly.
3. Add a new number using `add()`.
4. Remove an existing value with `remove()`.
5. Use `discard()` with a value that is not present.
6. Find the union and intersection of two sets.
7. Find the difference between two sets.
8. Convert a list with duplicate values to a set.

## Concept questions

1. What is a key–value pair?
2. Why can a dictionary contain another dictionary?
3. What is the difference between `keys()`, `values()`, and `items()`?
4. Why does `{}` create a dictionary instead of a set?
5. Why do sets not support indexing?
6. What is the difference between `remove()` and `discard()` in a set?
7. Compare lists, tuples, dictionaries, and sets.

---

# Final Learning Checklist

After studying these notes, you should be able to:

- [ ] Explain what a dictionary is and identify keys and values.
- [ ] Create dictionaries containing lists and nested dictionaries.
- [ ] Access values using keys and safely handle missing keys.
- [ ] Use `keys()`, `values()`, `items()`, and `update()`.
- [ ] Add, update, loop through, and remove dictionary entries.
- [ ] Explain what a set is and why duplicates are removed.
- [ ] Create an empty set correctly using `set()`.
- [ ] Add and remove set elements using `add()`, `remove()`, and `discard()`.
- [ ] Perform union, intersection, difference, and symmetric difference.
- [ ] Explain the difference between lists, tuples, dictionaries, and sets.

**Suggested GitHub location:** `Notes/04_Dictionaries_and_Sets.md`

**Suggested code location:** `Codes/dictionary_set_practice.py`
