#WAP to sum of n positive integers
n = int(input("Enter the number of positive integers to sum: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of the first", n, "positive integers is:", sum)
#summision of n numbers in a list and terminate the loop when user enters negative number
numbers = []
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    numbers.append(num)
print("The sum of the entered numbers is:", sum(numbers))
#for just the sum of numbers in the list 
"""_________BASIC METHOD_________"""
n = int(input("enter range of list: "))
list1 = []
sum = 0
print("elements of list")
for i in range(0, n):
    list1.append(int(input()))

for j in range(len(list1)):
    sum += list1[j]
print("Sum =", sum)
"""-----------------it can also be done this way-----------------"""
n = int(input("enter range of list: "))
list1 = []
print("enter the value of lists")
for i in range (0,n):
    list1.append(int(input()))
print("sum=",sum(list1))#sum is the predifined function to fins sum of all values in a list
