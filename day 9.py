l = ["Pavan", "Mani", 101, "Jai", "Pavan", "Jai", 101, "Harish", "Pavan", "Kiran"]
print (l)
print(len(l))
print(l.count("pavan"))
print(l.index("Jai"))

l1=[90,23,43,55,24,67]
print(max(l1))
print(min(l1))
print(sum(l1))

l.append("babu")
print(l)

l.extend("vani")
print(l)
l.insert(3,"lakshmi")
print(l)
l.pop(8)
print(l)

l.clear()
print(l)

t = ("Lakshmi", "Mani", "Lakshmi", 101, "Harish", "Kiran")
print(t, type(t))
print(t[1])
print(t[1:4])

for z in t:
    print(z)

t1=("karan",)
print(t1,(type(t1)))

print(len(t))
print(t.count('101'))
print(t.index('101'))
