# A. List Programs
# 1. Sum of List Elements
# 2. Average of List Elements
# 3. Maximum Element in a List
# 4. Minimum Element in a List
# 5. Count Even and Odd Numbers in a List
# 6. Reverse a List
# 7. Linear Search in a List
# 8. Bubble Sort a List
# 9. Count Occurrence of an Element in a List
# 10. Second Largest Element in a List
# B. Tuple Programs
# 11. Sum of Elements in a Tuple
# 12. Swap Two Tuple Elements
# 13. Find Max and Min in a Tuple
# 14. Convert List to Tuple and Tuple to List
# 15. Concatenate Two Tuples
# C. Iterative Loop Programs (Numeric)
# 16. Check Prime Number
# 17. Check Armstrong Number
# 18. Check Palindrome Number
# 19. Sum of Digits of a Number
# 20. Factorial of a Number
# 21. Fibonacci Series
# 22. Multiplication Table
# D. Conditional Expression / Statement Programs
# 23. Largest of Three Numbers (Conditional Expression)
# 24. Check Leap Year (Conditional Expression)
# 25. Grade Calculation (if-elif-else)
#------------------------------------------
"""Solution of 1st: Sum of list elements"""
list1=[]
a=int(input("enter the size of list: "))
for i in range(a):
    list1.append(int(input("enter element")))
print("Sum of list elements:", sum(list1))
#------------------------------------------

""" 2. Average of List Elements"""
list1=[]
a=int(input("enter the size of list: "))
for i in range(a):
    list1.append(int(input("enter element")))
avg=float(sum(list1)/a)
print("Average of list elements:", avg)
#------------------------------------------

"""Maximum Element in a List"""
print("Maximum Element in a List")
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
print("Maximum element in the list is:", max(list1))
#------------------------------------------

"""Minimum Element in a List"""
print("Minimum Element in a List")
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
print("Minimum element in the list is:", min(list1))
#------------------------------------------
"""Count Even and Odd Numbers in a List"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
e=0
o=0
for j in range (n):
    if(list1[j]%2==0):
        e+=1
    else:
        o+=1
print("even=\t", e)
print("odd=\t", o)
#------------------------------------------
"""Reverse of list"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
list1.reverse()
print("Reversed list:", list1)
#------------------------------------------
"""Linear Search in a List"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
t=int(input("enter the target value"))
for j in range(n):
    if(list1[j]==t):
        print("target found at positon,\t",j)
        k=0
        break
    k=1
if(k==1):print("not found")    
#------------------------------------------

""" 8. Bubble Sort a List"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
print("Original list:", list1)

for i in range(n):
    for j in range(0, n-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("Sorted list:", list1)
#------------------------------------------

""" Count Occurrence of an Element in a List"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
c=0
t=int(input("enter the value occourence to be counted"))
for j in range(n):
    if(list1[j]==t):
        c+=1
print(c,"-is the occourence of a particular element in list")
#------------------------------------------

""" second largest Element in a List"""
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
print("Original list:", list1)

for i in range(n):
    for j in range(0, n-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("Sorted list:", list1)
print("Second largest element:", list1[n-2])
