
# Use While loop with cdn and with undefined iteration.
count = 0
while count <= 3: print(count); count += 1

print("*******************")

# Count Down using While loops
countdown =10
while countdown >= 0:
  print (countdown)
  countdown = countdown - 1
print("We have liftoff!")

print("*******************")
kids = ["David","Kevin","Joel","Dany","Jeremy"]

#Using len() to loop through the list
#It behaves like Definite Loop though using while

index = 0
length=len(kids)

while index < length:
  print("kid No",index+1 ,kids[index])
  index += 1

print("*******************")

#Using Break
lookingFor = "Dany"
for kid in kids:
  if kid == lookingFor:
    print("I found out Dany!")
    break

print("*******************")
#Get the account no until the condition is met.
account_no = int(input("Account No: "))
while len(str(account_no)) != 12:
  print("Invalid Account No.")
  account_no = int(input("Account No: "))

print(" Thanks for your account Number:",account_no)


# Validate a Keyed in account no with an already existing account no.