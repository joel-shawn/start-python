course = {"Ruth":"Medicine", "David":"Engineering", "Jere": "Medicine", "Joan": "Medicine","Kevin":"Engineering","Joel":"Engineering"}

#Access the Values
print("Ruthie's course:", course["Ruth"])
print("David's course:", course["David"])
print("Jere's course:", course["Jere"])
print("Joan's course:", course["Jere"])
print("Kevin's course:", course["Kevin"])
print("Joel's course:", course["Kevin"])

#Try to access Unknown Key
#print("Dany's course:", course["Dany"])

#Adding a new item
#Dict[new_key] =new_value

course["Hannah"] = "Medicine"
course["Dany"] = "Medicine/Engineering"
course["George"] = "Nursing"

print("course", course)

#Delete an item  from the dictionary
del course["George"]
print("course after deletion", course)

#Update an item in the dictionary
course["Hannah"] = "Medicine/Scientist"
print("course after update", course)


course["Jeremy"] = "Medicine"
course["Jael"] = "Medicine/Scientist"

print("course after final addition ", course)


#Deleting the dictionary
del course
#print("course after dictionary deletion ", course)
