kids_list = ['David', 'Daniel', 'Hannah', 'Ruth', 'Kevin', 'Jere', 'Jael', 'Joel', 'Joan']
num_list = [1,7,84, 98.4, 34, 12, 57, 99.00, 64,99,99.0]
num_list1 = [3,"Jael"]


#List Size
print("length of the list", len(kids_list))

#List Max Value  - Goes by Alphabets
print("Max of the list", max(kids_list))

# High Preference for Float.99.00 and 99.0 are the same floating-point value.
# Python normalizes how floats are displayed, so you’ll always see 99.0
print("Max of the Number list", max(num_list))

# Cant Compare Int and String
#print("Max of the Number list1", max(num_list1))

#List Min Value  - Goes by Alphabets
print("Min of the list", min(kids_list))
print("Min of the Number list", min(num_list))

myname= ('A','B','C','D','E','F')
converted_list = list(myname)
print("Tuple to List:" , converted_list)


#Sorting
print ("Sorted \n")
print (sorted(kids_list))
print (sorted(num_list))
