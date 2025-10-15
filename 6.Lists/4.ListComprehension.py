numlist = [1,2,3,4,5,6,7,8,9]
squarelist =[]


#For Loop Approach - Creating a new list with the squares

for num in numlist:
    squarelist.append(num*num)

print(squarelist)

#List Comprehension Approach - Creating a new list with the squares

new_squarelist = [num*num for num in squarelist]
print("Squared List Using Comprehension :" ,new_squarelist)

new_squarelist = [num*num for num in squarelist if num%2==0]
print("Squared List Using Comprehension for even numbers:" ,new_squarelist)