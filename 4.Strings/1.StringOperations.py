#String Concatenation

welcome_msg = "Hello World\t" + "Python is exciting"
print (welcome_msg)


# Length of the string - Includes space as well
name1 = "Jere Irene"
print("String Len:", len(name1))


# First Character index = 0 and it goes on - Subscript Operator []
name2 ="Joan Blessy"
print ("Character at index ", 0 ,name2[0])
print ("Character at index ", 5 ,name2[5])

# Last Character index is -1 and it goes on
print ("Character at index ", -1 ,name2[-1])
print ("Character at index ", -5 ,name2[-6])

name3 = "Ruth Irene"

#Subscript of the string

print("Full Name:", name3[0:])

print("First Name:", name3[0:4])

print("Middle Name:", name3[5:10])
print("Middle Name:", name3[5:])


name4 ="Jael"

print("Alternative skip",name4[::2])
print("Alternative skip",name4[-4::2])

# Print Full Name
print("Full Name",name4[::])

# Reverse print Full Name
print("Reverse Name",name4[::-1])

# int to String
marks = 100
marks_str = str(marks)
print (marks_str, type(marks_str))



