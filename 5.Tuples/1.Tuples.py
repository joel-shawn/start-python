myTuple = (1, 2, 3, 4, 5.0,5)
myTuple1 = ("Adam", "Benjamin", "Caleb", "Daniel","Angel")
print(myTuple)
print(type(myTuple))

#Accessing values from the Tuple
print(myTuple[1])
print(myTuple[-1])

#Slicing

print(myTuple[1:4])
print(myTuple[-2:])

#Assigning Values to variables from Tuples
a, b, c, d, e,f = myTuple
print(a, b, c, d, e)

#length of the tuple
print("Length:" ,len(myTuple))

#Min of the tuple .
print("Min:" ,min(myTuple))

#Max of the tuple. Look carefully - First occurence is taken into account
print("Max:" ,max(myTuple))

#Min of the tuple . Based on the first Alphabet Character
print("Min:" ,min(myTuple1))

#Max of the tuple. Based on the first Alphabet Character
print("Max:" ,max(myTuple1))

# String To Tuple
name1 = "Jeremy"
myNewTuple =tuple(name1)
print(myNewTuple)

#Returns a list
print(sorted(myTuple1))

#Can Delete Tuple using the del key word.
del myNewTuple

#print(myNewTuple)