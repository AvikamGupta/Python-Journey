#check number of integers in a range divisible by 6
b=int(input("Enter the ending number of the range if initial is 1: "))
c=0
for i in range(1,b+1):
    if i%6==0:
        c+=1
print(c)

#2)Sum the all odd numbers and even number in the given input range N
a=int(input("enter the range of numbers from 1"))
sum1=0
sum2=0
i=1
for i in range(1,a+1):
    if(i%2==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
print("even=",sum1)
print("odd=",sum2)
#3) fibonacci series
a=int(input("enter the range for fibonacci series"))
b=1
c=1
print(b,c,end="")
while(b+c<=a):
    d=b+c
    print(d,end="")
    b=c
    c=d
#ibonacci in 2nd way
N = int(input("Enter the range for Fibonacci series: "))
fib_series = [0, 1]   # start with first two numbers
i = 1

while fib_series[i] + fib_series[i-1] <= N:
    fib_series.append(fib_series[i] + fib_series[i-1])
    i += 1

print("Fibonacci series up to", N, ":", fib_series)


#print only odd numbers as random numbers IN A GIVEN RANGE
from random import random, randrange
print(randrange(1,20,2))
#print only even numbers as random numbers IN A GIVEN RANGE
print(randrange(2,21,2))
# #random function print between (0.0 to 1.0)
print(random())
