#String Replace

welcome_msg = "Welcome to Python World. It is exciting to learn. Do you think it is exciting ?"
print(welcome_msg)

print("Replace one occur" ,welcome_msg.replace("exciting","interesting",1))
print("Replace all occurs" ,welcome_msg.replace("exciting","interesting"))


# Creates a list of splitted strings
welcome_list = welcome_msg.split()

# Join these list of strings in the list
print("Hypen:","-".join(welcome_list))
print("NoSep:","".join(welcome_list))
print("Spaces:","    ".join(welcome_list))

