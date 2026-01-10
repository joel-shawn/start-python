"""
Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
Access Key: Print the value associated with the city key.
"""


print("exercise 1")
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print(my_dict)

my_dict["profession"]="doctor"
print("updated dictionary after adding profession:",my_dict)

my_dict["age"]="40"
print("modified dictionary after modification:",my_dict)

print("city:",my_dict['city'])
"""
Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
Check if Key Exists in the dictionary
"""

print("exercise 2")
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print(my_dict)

my_dict.pop('profession')
print("Updated dictionary after removing 'profession'",my_dict)


for key, value in my_dict.items():
    print(key, value)

print("does age exist:",'age' in my_dict)
"""
Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.

"""
print("exercise 3")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

"""
Clear all key-value pairs from a given dictionary and print it."""
print("exercise 4")
my_dict.clear()
print(my_dict)
"""
Write a code to merge two dictionaries into a new dictionary and print it.
"""
print("exercise 5")

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)

"""
Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.
"""
print("exercise 7")

data = {'person': {'name': 'Alice', 'age': 30}}
print(data)

print(data['person']['age'])
"""
expected output
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}"""
print("excersise 8")

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict)

print(sampleDict['class']['student']['marks']['history'])

"""
In the below dictionary, change name to ‘Jessa’.
"""
print("exercise 9")

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict['class']['student']['name']="jessa"
print(nested_student_dict)
"""
In Python, we can initialize the keys with the same values.
"""
print("excercise 10")

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees, defaults)
print(result)


"""
Delete a list of keys from a dictionary
"""
print("excercise 12")

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
"""
While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

Write a Python program to check if the value 200 is present in the provided dictionary.
"""
print("excercise 13")

n_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in n_dict.values():
    print('200 present in a dict')
"""
Write a program to rename a key city to a location in the following dictionary.
"""
print("excercise 14")
ex_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
ex_dict['location'] = ex_dict.pop('city')
print(ex_dict)
"""
Write a code to print the key of a minimum value from the following dictionary.
"""
print("excercise 15")
new_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(new_dict, key=new_dict.get))
"""
Write a Python program to change Brad’s salary to 8500 in the following dictionary.
"""
print("excercise 16")
edit_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

edit_dict['emp3']['salary'] = 8500
print(edit_dict)
"""
Write a code to swap keys and values in a dictionary. Assume all values are unique
"""
print("excercise 17")

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

swapped_dict = dict(zip(original_dict1.values(), original_dict1.keys()))
print("original dict",original_dict1)
print("swapped dict", swapped_dict)
"""
Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
"""
print("excercise 18")

l_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}


sorted_dict = sorted(l_dict.items())

print(sorted_dict)
"""
Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
"""
print("excercise 20")

def are_values_unique(d):

    return len(d.values()) == len(set(d.values()))


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 10, 'y': 20, 'z': 10}
dict3 = {}


print(are_values_unique(dict1))
print(are_values_unique(dict2))
print(are_values_unique(dict3))




