welcome_msg = "Welcome to Python 3 World It is exciting to learn Do you think it is exciting"
welcome_note = "Python3Users "
welcome_space = " "


#starts with
print("Does it start with Welcome ?" ,welcome_msg.startswith("Welcome"))
print("Does it start with Welcome ?" ,welcome_msg.startswith("Welcome",5,13))

#ends with
print("Does it end with exciting ?" ,welcome_msg.endswith("exciting"))

print("Does it contain only strings ?" , welcome_note.isalpha())
print("Does it contain only numbers ?" ,welcome_note.isdigit())
print("Does it contain only alpha + numbers ?" ,welcome_note.isalnum())
print("Does it contain space ?" ,welcome_space.isspace())
print("Does it contain Title Pattern?" ,welcome_note.istitle())
print("Does it contain All  Upper Case?" ,welcome_note.isupper())
print("Does it contain All  Lower Case?" ,welcome_note.islower())




