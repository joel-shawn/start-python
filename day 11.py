s=set()
print(s,type(s))


s1={101, 'Kiran', 'Jai', 'Ravi', 25.67, 'Mani'}
print(s1)
s1.update({"Harish", 100, "Dilip"})
print(s1)
s1.remove(101)
print(s1)
s1.discard('Jai')
print(s1)

print(len(s1))


s1 = {"Kiran", 45.34, "Mani", "Jai"}
s2 = {"Mani", 101, "Priya"}
ns = s1. union (s2)
print(ns)

s1 = {"Kiran", 45.34,"Mani"}
s2 = {"Mani", 101, "Priya"}
ns = s1. difference(s2)
print(ns)
ns1 = s2. difference(s1)
print(ns1)



"""
1. WAP to convert list of values into a string ?(1 = ["P", "y", "t", "h", "o", "n"])
o/p: python
2. WAP to multiply all the values given in tuple?(t = (3,1,6,4,5,7,2))
o/p: 5040
3. WAP to display all names from the given list that are starting wit "R"?
(1=["Akash", "Rocky", "ram", "Bablu", "Rakesh"])
o/p: Rocky Rakesh

"""

#1
s=["P", "y", "t", "h", "o", "n"]
string ="".join(s)


#2
t=(3,1,6,4,5,7,2)

product =1
for i in t:
    product *=i

print(product)


#3
l=["Akash", "Rocky", "ram", "Bablu", "Rakesh"]
for name in l:
    if name.startswith("R"):
        print(name)


