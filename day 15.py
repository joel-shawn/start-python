import math as m
import random as r

n = int(input("enter integer value:"))
print(m.factorial(n))


## fLoor() - return Lower integer
n = float(input("enter float value:"))
print (m. floor (n))

## ceil() - return greater integer
n = float(input("enter float value:"))
print(m.ceil(n))

n = float (input ("enter float value:"))
print(m.round(n))

n = float(input("enter negative float value:"))
print (m. fabs (n))

n1 = int(input("enter integer value:"))
print(m.sqrt(n1))

n1 = int(input("enter integer value:"))
print(m.exp(n1))

num = int(input("enter integer value:"))
den = int(input("enter integer value:"))
print(m. fmod (num, den))

base = int(input("enter integer value:"))
p = int(input("enter integer value:"))
print(m. pow(base, p))
print(base**p)



z = m.pi
print(z)
z += 1
print(z)
print(m.pi)

print(m.e)
print(m.tau)

print (r.random())
print(r.randint(1,6))

user = input("enter your choice:")
print("Users choice:", user)
machine = r.choice(["paper", "rock", "scissor"])
print ("Machine Choice:", machine)