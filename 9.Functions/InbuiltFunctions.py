#Character Values --> Ascii Code
print(ord("P"))

#From Ascii Code --> #Character Values
print(chr(47))
print(chr(57))

# Length of the string
name1 = "Jeremah"
print("String Len:", len(name1))

#Based on Ascii Value
print("Min Character", min(name1))
print("Max Character", max(name1))

print("J" , ord("J"))
print("r" , ord("r"))

marks = 100
marks_str = str(marks)
print (marks_str, type(marks_str))

#import cytpes
#ctypes.cast(1234556,cytypes.py_object).value

list_one = [1, 2, 3]
list_two = str(list_one)
print(type(list_one))
print(type(list_two))

welcome_msg ="Welcome to Python World"

# Use the in operator
if "Welcome" in welcome_msg:
    print("Welcome !")

x="Kevin"
print("Is it a string instance :" ,isinstance(x, str))
