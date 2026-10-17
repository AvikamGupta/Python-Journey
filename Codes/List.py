#list practice
marks=[1,2,3,4,5]
print(marks)
print(marks[0]+marks[4])
print(len(marks))
#list slicing
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])
marks.append(6)
print(marks)
marks.insert(3,9)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.remove(9)
print(marks)
marks.pop(4)
print(marks)
#palindrome list check
print('ENTER number of ARRAY ELEMENTS')
n=int(input())
list=[]
print("fill the array")
for i in range(n):
    list.append(int(input()))
list2=list.copy()
if(list[:n]==list2[::-1]):
    print("it is palindrome")
else:
    print("not") 
#tuples
tup=(1,2,3,4)
print(type(tup))
print(tup[2])
