#String Split methods

order = "SG-MODEL:12345-CLAY"

# Splits based on delimiter and returns a list
print(order.split('-'))

model = order.split('-')
print("Model Number:" ,model[1])

# Splits based on space delimiter when not specific and returns a list
order1 = "Lego Toy"
print(order1.split())


# String justify

text = "Python"
text2 = "is cool"
# Uses * to fill the characters
print("Left Just 10:",text.ljust(10, "*"))

# Uses * to fill the characters - Nothing Happens
print("Left Just 5:",text.ljust(5, "*"))

# Uses space by default to fill the characters
print("Left Just 20:",text.ljust(20) + text2)

# Uses * to fill the characters - Right Just
print("Right Just 10:",text.rjust(10, "*"))
print("Right Just 15:",text.rjust(15, "*"))

# Uses * to fill
print("Center Just :",text.center(13, "*"))
print("Center Just :",text.center(13))


#String Fill Method - Can also use ljust instead
account_number ="123456"
print(account_number.zfill(10))