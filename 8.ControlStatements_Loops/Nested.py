kids = ["David","Kevin","Joel","Dany","Jeremy"]
print("********************")

for name in kids:
    for char in name:
        if char == "e":
            print ("Only",name , " has a character 'e'")
            break
print("********************")

#Print Kids who doesnt have the character e in their names
for name in kids:
    if (name.count("e") == 0):
        print (name , " doesnt have character 'e'")