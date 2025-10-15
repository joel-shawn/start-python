#Functions that can be applied to Dictionary
course ={'Ruth': 'Medicine', 'David': 'Engineering', 'Jere': 'Medicine', 'Joan': 'Medicine', 'Kevin': 'Engineering', 'Joel': 'Engineering', 'Hannah': 'Medicine/Scientist', 'Dany': 'Medicine/Engineering', 'Jeremy': 'Medicine', 'Jael': 'Medicine/Scientist'}

#Number of Items in the dictionary
print("Dictionary - Number of Items ", len(course))
print(type(course))
print(course)

#Converting a dict into String
course1= str(course)
print (type(course1))
print(course1)


#try accessing data as if you access dictionary . You cant access.because it is a string
#print(course1["Ruth"])

#Max of Key Values
print("Max of key values :", max(course))

#Max of Key Values
print("Min of key values :", min(course))


sample_tuple =[("A","Apple"),("B","Banana"),("C","Cherry")]
sample_list =[["A","Apple"],["B","Banana"],["C","Cherry"]]


print("Dictionary - Sample Tuple: ", dict(sample_tuple))
print("Dictionary - Sample List: ", dict(sample_list))

#Checks the existence of the key

if "Ruth" in course:
    print("Yes she has decided on her course:" , course['Ruth'])

if "Ayya" not in course:
    print("Ayya  has not taken any course:")