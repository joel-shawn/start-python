#intializing a list
empty_list = []
my_list = ["David","Daniel","Hannah","Ruth","Kevin"]
my_list1 = ["Jere", "Jael","Joel","Joan"]

#Combining Two Lists. No Impact on Original list
print("Combined Lists" , my_list + my_list1)
print("Original List1" , my_list)
print("Original List2" , my_list1)

#  Multiplying the list # Check the memory address using id(object)
multplied_list = my_list*3
print("Multiplied One:" , multplied_list)

# Assigning list values to variables
kid1,kid2,kid3,kid4,kid5 = my_list
print("Kid3:::",kid3)

#accessing the lists values
print("Accessing Specific Value:",my_list[0])
print("\n")


#Slicing a list
print(my_list[1:3])
print(my_list[:2])
print(my_list[:])
print("Skipping by 2", my_list[0::2])
print("\n")
print("List Now--" ,my_list)

#updating a list - Updates the original list
my_list[3] = "Ruthie"
print("After updating :" ,my_list)
print("\n")

#Deleting items from a list. Deletes from the original list
del my_list[2]
print("After Deletion 3rd Item:" , my_list)

del my_list[1:2]
print("After Deleting Couple of Items" ,my_list)

#You may assign the combined list into new
final_list = my_list + my_list1
print("My Final List:" , final_list)



print("List Now" ,my_list)
# Check for a presence of value in list
if "Pops" in my_list:
    print("Not In here")
if "David" in my_list:
    print("Yes he is in here ")

print("-".join(my_list))