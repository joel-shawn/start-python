s = "welcome to Python classes @ Besant Technologies"
print( type(s))

print(s.index("B"))
print(s.index("t",14))
print(s[33:27:-1])

for z in s:
    print(z,end="")
print(s.count("e"))

s1 = "Dilip"
s2 = "Kumar"
ns = s1+""+s2
print(ns)

## title() - v_n.title()
s= "weLcome to pyThON, clASSes"
print (s)
s1 = s.title()
print ( s1)
print(s)

s = "Hello Everyone! welcome to besant technologies"
print(s)
l = s.split("e") #List
print(l, type(l))