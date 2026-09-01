#to print the elements of a list using while loop
list1 = [1, 2, 3]
i=0
while i < len(list1):
    print(list1[i])
    i += 1
#same above program using while loop with 2d array
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0
while i < len(list2):#this loop acceses the values of the list2
    j = 0
    while j < len(list2[i]):#this loop acceses the values of the list2[i]
        print(list2[i][j], end="\t")  # Print elements in the same row separated by a tab
        j += 1
    i += 1
    print()  # Print a newline after each row
