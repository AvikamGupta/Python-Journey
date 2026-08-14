print("My name is Avikam")
print("I am learning", "basic programming of Python")

age = 18
name = "Avikam"

print("My name was:", name)
print("My age is =", age)

# -------------------------------
# Basic Variables and Operators
# -------------------------------

a = 5
b = 2
var3 = a * b

print(a)
print(b)
print(var3)

print(a > b)
print(b > var3)
print(var3 > b)

print(type(name))
print(type(age))

print(a ** b)  # a to the power b

# -------------------------------
# Logical Operators
# -------------------------------

print("AND operator:", (a > b) and (b == a))
print("OR operator:", (a > b) or (b == a))
print("NOT operator:", not (a > b))

# -------------------------------
# Type Casting and Conversion
# -------------------------------

a = 2.4
b = int("3")

print(a + b)
print(type(b))

# -------------------------------
# Input Function
# -------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentile = float(input("Enter the percentile: "))

print("Welcome", name)
print("Age =", age)
print("Percentile =", percentile)
