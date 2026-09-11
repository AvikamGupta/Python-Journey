#WAP to execute fibonnaci seies for n value using functions demonstrate the same in all the four types of functions
#fn. without arguement and without return type
def fibo1():
    n=int(input("enter the number of terms"))
    a=1
    b=1
    print(a)
    print(b)
    while(n<=a+b):
        c=a+b
        print(c)
        a=b
        b=c
#fn.with return type and without arguement
def fibo2():
    n=int(input("enter the number of terms"))
    a=1
    b=1
    fibo_series=[a,b]
    while(n<=a+b):
        c=a+b
        fibo_series.append(c)
        a=b
        b=c
    return fibo_series
#with arguement and without return 
def fibo3(n):
    a=1
    b=1
    print(a)
    print(b)
    while(n<=a+b):
        c=a+b
        print(c)
        a=b
        b=c
#fn.with both arg and return type
def fibo4(n):
    a=1
    b=1
    fibo_series=[a,b]
    while(n<=a+b):
        c=a+b
        fibo_series.append(c)
        a=b
        b=c
    return fibo_series
