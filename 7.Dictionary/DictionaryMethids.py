course1 ={'Ruth': 'Medicine', 'David': 'Engineering', 'Jere': 'Medicine', 'Joan': 'Medicine', 'Kevin': 'Engineering', 'Joel': 'Engineering', 'Hannah': 'Medicine/Scientist', 'Dany': 'Medicine/Engineering', 'Jeremy': 'Medicine', 'Jael': 'Medicine/Scientist'}
print("Course1 ID", id(course1))

#Copy
#Has the same memory address as 1
course2 = dict.copy(course1)
print("Course2", course2)
print("Course2 ID ", id(course1))

#Has the different memory address as 1
course3 = course1.copy()
print("Course3", course3)
print("Course3 ID ", id(course3))

#Using the same assignment operator -Has the same memory address as 1
#and updating one dictionary updates the other dictionary too
course4 = course1
print("Course4", course4)
print("Course4 ID ", id(course4))

course1["Jeremy"] = "Engineering"

print("Course1", course1)
print("Course2", course2)
print("Course3", course3)
print("Course4", course4)

#Validate the ID for the 1st dict and dict created by assignment operation

print("Course1==>", id(course1))
print("Course2", id(course2))
print("Course3", id(course3))
print("Course4==>", id(course4))

# Trying to get the key value wherein the key doesn't exist in the dictionary.
#Key Error - Try this
#print("George Course", course1["George"])

print("George Course:::", course1.get("George","Not found"))
#If no custom message - then returns None
print("George Course:::", course1.get("George"))


#Set Default Value Method for a key .Observe that key has been added into the dictionary
course1.setdefault("George","Not found")
print("course", course1)

course1.setdefault("Issac")
print("course", course1)


# Look for the list of keys
print("Keys", course1.keys())

# Look for the list of values of the dictionary
print("Values", course1.values())


# Combining two dictionaries
sample_dict1 ={"A":"Apple","B":"Banana","C":"Cherry"}
sample_dict2 ={"W":"WaterMelon","O":"Orange"}

print("sample_dict3", sample_dict1.update(sample_dict2))
print("sample_dict1", sample_dict1)
print("sample_dict2", sample_dict2)

# Returns the list of dictionary( key value ) Tuple pairs
print("sample_dict1", sample_dict1.items())

#Clear the dictionary values.
print("sample_dict2:::", sample_dict2.clear())
print("sample_dict1", sample_dict2)