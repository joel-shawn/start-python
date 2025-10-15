#Actual Function
def trip_welcome():
  print("Welcome to the trip !")
  print("Let's get started.")

#Function Call
trip_welcome()

print("****************************************")

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:
#Function Call with no parameters
directions_to_timesSq()

print("***************************************")


def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit" ,location)
  print("You can use the public subway system to get to", location)

# Call your function here:
#Function Call with single parameters
generate_trip_instructions("Grand Central Station")

#try Calling this without parameter
#generate_trip_instructions()


print("****************************************")

# Write your code below:
car_rental_total = 0
hotel_total = 0

def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate,trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total =   car_rental_total + hotel_total + plane_ticket_price

  # Returning a value back to caller
  return trip_total

# Call your function here:
#Function Call with multiple parameters. It returns a value
print("Total Cost ", calculate_expenses (200,100,100,5))

print("****************************************")

#Function with Default Values -Effective when no values are passed
def trip_planner1(first_destination,second_destination,final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in" , first_destination, "then" , second_destination, "and lastly" ,final_destination)

#Try with just parameters. Default Value takes effective
trip_planner1("Denmark", "France", "Germany")
trip_planner1("Denmark", "France")

print("****************************************")

#Function with Keyed Arguments - Order doesnt Matter
def trip_planner2(first_destination = "Iceland",final_destination = "Germany",second_destination = "India"):
  print("Here is what your trip will look like!")
  print("First, we will stop in" , first_destination, "then" , second_destination, "and lastly" ,final_destination)

trip_planner2()

print("****************OBSERVE************************")

def trip_planner(first_destination = "Iceland",final_destination = "Germany",second_destination = "India"):
  print("Here is what your trip will look like!")
  print("First, we will stop in" , first_destination, "then" , second_destination, "and lastly" ,final_destination)

# This Value is effective and prioritized - The positional one
trip_planner("Brooklyn","Queens")

print("****************************************")

shirt_expense = 9
current_budget = 3500.75

def deduct_expense(budget,expense):
  return budget - expense

new_budget_after_shirt = deduct_expense(current_budget,shirt_expense)

print(new_budget_after_shirt)

print("****************************************")
#Return Multiple values
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first,second,third

most_popular1,most_popular2,most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

print("****************************************")

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 ",name)

trip_planner_welcome("Peace")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(4.5)

def destination_setup(origin,destination,estimated_time,mode_of_transport="Car") :
  print("Your trip starts off in" ,origin)
  print("And you are traveling to ", destination)
  print("You will be traveling by ", mode_of_transport)
  print("It will take approximately ", estimated_time ,"hours")

destination_setup("SG","KMU",estimate,"Air India Express")
destination_setup("SG","KMU",estimate)

print("****************************************")

#Function with Variable length argument

def vararg (var1,*var2):
  print(var1)
  for var in var2:
    print(var)

vararg(60)
vararg(10,20,30)

def info(**country):
  print(country)
  for key,value in country.items():
    print(key,":::::",value)

info(India="Delhi",Sinnga="Singapore")


def createlist(list1):
  list.extend([10,20,30])
  print(list)


list1 =[40,50,60]
print(list1)
createlist(list1)
print(list)



