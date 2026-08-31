# print("class lectures practices only")
#WAP to check wether a number is even or odd
a=int(input("enter the number"))
if(a%2==0):
    print("even")
else:
    print("odd")
#WAP to check wether a number is +ve or -ve
b=int(input("enter the number"))
if(b>0):
    print("positive")
elif(b<0):
    print("negative")
else:
    print("zero")
#WAP to get marks of 3 subjects and if marks is greater than 50 in all subjects then print "pass" otherwise print "fail"
c=int(input("enter the marks of subject 1"))
d=int(input("enter the marks of subject 2"))
e=int(input("enter the marks of subject 3"))
if(c<50):
    print("fail in first subject")
elif(d<50):
    print("fail in second subject")
elif(e<50):
    print("fail in third subject")
else:
    print("pass")
