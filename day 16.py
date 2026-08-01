import collections as c

l = ["pavan", "Mani", "pavan", "pavan", "Sashi", "Mani"]
## count()
print(l.count ("pavan"))
print(l.count ("Mani"))
print(l.count("Sashi"))

l = ["pavan", "Mani", "pavan", "pavan", "Sashi", "Mani"]
x =c.counter(l)
print(x)



d1 = {"name": "Kiran", "age" :25}
d2 = {"course": "Python", "loc": "Bangalore"}
z = c. ChainMap(d1, d2)
print (z)

print(z['loc'])

def display():
    return "key does not exists."
d1 = c.defaultdict(display, {"name":"Kiran",})
print(d1["name"])
print(d1["age"])
print(d1["fees"])
