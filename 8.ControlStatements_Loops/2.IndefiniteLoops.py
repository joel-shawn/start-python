#  break the infinite loop using break
sum = 0
while True:
    number = int(input("Enter a Number: or Key-in 0 to quit: "))
    sum += number
    if number == 0:
        break

print("The Total Sum is ", sum)


#  break the infinite loop using break or some flag
sum = 0
flag = True
while flag:
    number = int(input("Enter a Number: or Key-in 0 to quit: "))
    sum += number
    if number == 0:
        flag = False

print("The Total Sum is ", sum)
#break only exits the innermost loop it belongs to.Here For Loop
kids = ["David","Kevin","Joel","Dany","Jeremy"]
found = False
while (not found):
    for kid in kids:
        if kid == "Dany":
            print("Yes Dany is in  here. Found him!")
            found = True
            break
        else:
            print("kid",kid)
    print("I am here")