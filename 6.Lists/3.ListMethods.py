country_list =[]
country_list1 = ["Canada","India","Russia"]

country_list.append("US")
country_list.append("London")
country_list.append("Singapore")

print("Current Country List:" ,country_list)

#See what happens if you  try to print this way - Why.. Append always returns None .but does some job.
print(country_list.append(country_list1))

# This is not what we want - It did the second list as one of the component of list1
print("After Appending:" ,country_list)

country_list2 = ['US', 'London', 'Singapore']

# Combining two lists
country_list1.extend(country_list2)
print("After Extending:" ,country_list1)

#You could have used + . But that doesnt update the original list. you might need to store in a new list.


#Extending with tuples
name =("Korea","Russia")
country_list1.extend(name)
print("After Extending with Tuple:" ,country_list1)

#Extending with String
country_list1.extend("Japan")
print("After Extending with String:" ,country_list1)


#count
print ("Russia occurs:" , country_list1.count("Russia"))

# whats the index of an item. Just prints the first occurence
print ("Russia at position :" , country_list1.index("Russia"))


#Insert. Updates the original list
country_list1.insert(0,"Australia")
print("After Inserting a new country at a specific location:" ,country_list1)


#Remove. Updates the original list
country_list1.remove("Russia")
print("After Removing Russia - Just removes first occurence :" ,country_list1)

#Pop.Returns the removed item - So ..Removes from the original list and returns from the original list
removed_item = country_list1.pop()
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)

removed_item = country_list1.pop()
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)

removed_item = country_list1.pop()
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)

removed_item = country_list1.pop()
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)

removed_item = country_list1.pop()
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)

removed_item = country_list1.pop(0)
print("Removed Item :"+removed_item ,":::Country List::" , country_list1)


#Sort
country_list1.sort()
print ("Sorted List :" ,country_list1)

#Sort and Reverse
country_list1.sort(reverse=True)
print ("Sorted and Reversed List :" ,country_list1)

#Reverse
country_list1.reverse()
print("Reversed List:", country_list1)

#List of tuples
name = [("Ruthie",1),("David",3),("Jere",2),("Joan",4)]

#For each tuple x, take its second element (x[1]) as the "sorting key". Syntax key=function
name.sort(key=lambda x:x[1])
print("Sorted using Key", name)

name.sort()
print("Sorted using Lexi Order", name)

