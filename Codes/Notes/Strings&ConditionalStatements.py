# ==========================================
# Python Journey - Day 2
# Topic: Strings & Conditional Statements
# ==========================================


# ------------------------------------------
# 1. Strings
# ------------------------------------------

str1 = "this is a string"
str2 = "VIT"
str3 = """this is a string but in triple quotes"""


# ------------------------------------------
# 2. Escape Characters
# ------------------------------------------

str4 = "this is a string\nin python"
print(str4)


# ------------------------------------------
# 3. String Concatenation
# ------------------------------------------

print(str1 + str2)
print(str1 + " " + str2)


# ------------------------------------------
# 4. Length of a String
# len() returns the number of characters,
# including spaces.
# ------------------------------------------

print(len(str1))
print(len(str2))
print(len(str3))


# ------------------------------------------
# 5. String Indexing
# Indexing starts from 0.
# ------------------------------------------

print(str2[1])


# ------------------------------------------
# 6. String Slicing
# The ending index is not included.
# ------------------------------------------

print(str3[3:7])
print(str3[3:len(str3)])

# If the ending index is omitted,
# Python continues until the end.
print(str3[2:])


# ------------------------------------------
# 7. Negative Indexing
# The last character has index -1.
# ------------------------------------------

print(str2[-3:-1])


# ------------------------------------------
# 8. String Functions
# ------------------------------------------

str5 = "i am studying python from apna college"

# Check whether the string ends with a specific value
print(str5.endswith("ege"))

# Capitalize the first character
print(str5.capitalize())

# Replace one value with another
print(str5.replace("o", "a"))

# Find the first occurrence of a value
# Returns -1 if the value is not found
print(str5.find("o"))

# Count the number of occurrences of a value
# Returns 0 if the value is not found
print(str5.count("am"))


# ------------------------------------------
# 9. If-Elif-Else
# ------------------------------------------

color = input("What is the colour of the traffic light: ")

if color == "red":
    print("Stop")

elif color == "yellow":
    print("Be ready to move")

else:
    print("Move")
