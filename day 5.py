#conditional statements

if 45==45:
    print("values are same")
else:
    print("values are different")

n=int(input("enter a value"))
if n<0:
    print("negative")
elif n==0:
    print("neutral ")
else:
    print("positive")

#logical operators
a=45
b=78
c=29
print(a>b and a>c)
print(b>a and b>c)
print(c>a and c>b)

if a>b and a>c:
    print("a has greatest value")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c has greates value")


l=(int(input("enter a number")))
if n%2==0or n%5==0:
    print("l is a multiple")
else:
    print("l is not a multiple")

#identity operators
a=19
b=34
c=67

print(id(a))
print(id(a))
print(id(a))