# Just with if/else
num = int(input("Enter a number :"))

if num % 2 == 0 :
  print("Even Number")
else:
  print("Odd Number")

# With if/elif/else
age = int(input("Age: "))
if age < 3:
  print("Baby")
elif age >= 3 and age >= 5:
  print("Toddler")
elif age < 13 and age > 5:
  print("Boy/Girl")
elif (age >= 13 and age <= 18):
  print("Teen")
elif (age > 18 and age <= 22):
  print("Young Adult")
elif (age > 22 and age <= 60):
  print("Adult")
else:
  print("Elderly Man")