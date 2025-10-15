#Prints just an object in Python3 unlike python2
print (range(10))

#List + Range
print (list (range(10)))
print (list (range(0,10)))
# Skip in 5s
print (list (range(5,16,5)))


print("*******************")
#Always on a new line
for i in range(10):
  print(i)


# on Same line with space

for i in range(10):
  print (i, end=" ")

print("*******************")


kids = ["David","Kevin","Joel","Dany","Jeremy"]

# Simple For Loop in one line
for kid in kids: print (kid)

print("*******************")

#For Loop - defined number
for cnt in range(2):
  print ("I am trying to use range function + For Loops" , cnt+1)

print("*******************")


#List comprehension with For Loop

name_change = [kid + " Chellam" for kid in kids]
print(name_change)

for chr in "Godwin":
  print(chr,end=",")

# Print a user's preferred multiplication table
