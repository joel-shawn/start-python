name1 = "Adonai is the almighty and he is my boss"

#Count()

#Count the number of characters in the string
print ("Number of 'a's ",  name1.count("a"))

#Count the number of characters in the string
print ("Number of 'a's ",  name1.count('a',0,5))


#Find()

# Find a Substring/character in the string.
print ("Finding 'is' : ", name1.find("is",0))

# Provides the last occurence 's starting index of this subscript
print ("Finding 'is' : ", name1.rfind("is"))

#If the substring is not found, it returns -1 (instead of raising an error).
print ("Finding 'is' : ", name1.find("z"))


#index()

print ("Finding the index  : ", name1.index("i"))
print ("Finding the index  : ", name1.rindex("i"))

# Throws Error if the character/string is not found - So safe to use find instead of index
#print ("Finding the index  : ", name1.rindex("z"))



#Case conversion Methods

print ("Convert to ALL CAPS :", name1.upper())

print ("Convert to ALL LOWER CASE :", name1.lower())

print ("Convert to ALL CAPITAL CASE :", name1.capitalize())

print ("Convert to ALL CAMEL  CASE  ACROSS:", name1.title())

print ("SWITCH CASE  ACROSS:", name1.swapcase())


#String Strip Methods - Very useful to remove the starting trailing unnecessary characters from your string

orderID=" 124567n"
#Removes the 'n' from the right most
print(orderID.rstrip('7n'))

#Removes the space in the left
print(orderID.lstrip())

#Removes the space in the both sides
orderID=" 124567n "
print(orderID.strip())
