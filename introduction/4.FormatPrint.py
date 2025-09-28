
# Unformatted one
print("Name","Place","Age")
print("Ruthie","Canada",19)
print("Jere","India",18)
print("David","Canada",17)
print("Joana","India",17)
print("Kevin","Singapore",16)
print("Joel","Singapore",13)
print("Daniel","US",11)
print("Hannah","US",7)
print("Jeremy","US",6)
print("Jael","US",3)
print("----------------\n\n")


# Formatted one Method #1
# %-10s → left-align a string in a 10-character wide column.
# %5d → right-align an integer in a 5-character wide column.

print("%-10s %-10s %5s" % ("Name", "Country", "Age"))
print("%-10s %-10s %5d" % ("Ruthie", "Canada", 19))
print("%-10s %-10s %5d" % ("Jere", "India", 18))
print("%-10s %-10s %5d" % ("David", "Canada", 17))

print("----------------\n\n")
# Formatted one Method #2
#Here <10 means left-align in a 10-character column.

print(f"{'Name':<10}{'Country':<10}{'Age':<5}")
print(f"{'Jere':<10}{'India':<10}{18:<5}")
print(f"{'David':<10}{'Canada':<10}{17:<5}")

