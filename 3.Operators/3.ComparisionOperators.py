
x = z = 100
y = 200
value = "100"
name1 = "Kevin"
name2 = "Joel"

print("Greater:" ,x > y)
print("Smaller:" ,x < y)
print("Equal To:" ,x == z)
print("Not Equal To:" ,x != z)
print("Less than & Equal To:" ,x <= z)
print("Greater than & Equal To:" ,x <= z)

# This is equivalent to check (x<y) and (y<z)
print("Chained Comparisons:" ,x < y < z)

print (str(x) <= value)

# Different Data Types (int & string) ends up unequal
print (x == value)

# Different Data Types (int & float) ends up equal
print (4 == 4.0)
print (4.0000 <= 4)

# Higher the Alphabets greater it is  - Compared based on alphabetical order
print (name1>name2)

