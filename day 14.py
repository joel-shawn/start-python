import os

def fact(n): #n=5/4/3/2/1
    if n == 1: ## terminate case - 1==1
        return 1 #5*4*3*2*1

    else: ## recursive case
        return n*fact(n-1) #5*fact(4)=5*4*fact (3)=5*4*3*fact(2)=5*4*3*2*fact(1)
x = int(input("enter a integer value"))
print (fact(x))


def product(x,y):
    print(x*y)
product(3,10)

z=lambda n1,n2: n1*n2
print(z(10,3))


l=[1,2,3,4,5]
n1=list(map(lambda x:x**3,l))
print(n1)

li = [45, 11, 24, 36, 87, 9, 45, 33, 18, 30]
li1 = list(filter(lambda y:y%2!=0,li))
print(li1)

print(os.getcwd())


f = open ("sample.txt", "w")
f.write("Hello! EveryOne!")
f. close()
print(os.listdir())

f = open ("demo.doc", "a")
f.write("Python classes from Monday to Friday..")
f. close()

f = open ("demo.doc", "a") # filename exists -append
f.write("\nTimings: 8:00PM to 9:00PM")
f. close()

os. rename ("demo.doc", "new_demo.txt")
os.unlink("sample.txt")

