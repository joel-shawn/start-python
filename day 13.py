print("Welcome to python classes")
print("on weekdays from monday to fridays")
print("@Besant technologies")

def display():
    print("Welcome to python classes")
    print("on weekdays from monday to fridays")
    print("@Besant technologies")

n1=45
n2=9

print("Addition:",n1+n2)
display()

print ("Subtraction:",n1-n2)
display()

print("Multiplication:",n1*n2)
display()


name="BT"
time = "8:00PM"
def inform(name,time):
    print("my institute name is" ,name )
    print("my class timing is", time)
inform("besant technologies",8)
inform("Bt","eight pm")


def inform(name="No.1 institute", time="evening"):
    print("My institute name is", name)
    print("My class timing is", time)
inform ()
inform ("BT", "8PM" )
inform("Besant Technologies")
inform(time=8)


#variable arguement
def skills(*course):
    print(course)
skills("Python", "Java", "HTML" )

def addition(a, b):
    print ("welcome")
    return a+b
    print("Hi")
print (addition (100,9))
print ("welcome")

def details():
    yield("Hello everyone")
    l= ["pavan","Kiran",101,"Mani"]
    yield l [-1]
    yield 34*2

for x in details():
    print(x)
