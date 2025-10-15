name1 = "Jeremy"
name2 = "Jeremy"

#Comparing the same value
print (name1 == name2)

# Object Reference - Looks Same
print (name1 is name2)
print(id(name1))
print(id(name2))


x = 10
y = 10
z = 100/10

# Object Reference - Looks Same 0 - 256
print (x == y)
print (x is y)
print (x is not y)

# Object Reference - Different ID

print(id(x))
print(id(z))
print (x is z)

# Object Reference - May or May not be the same. after 256

num3=685
num4=685
print(id(num3))
print(id(num4))



