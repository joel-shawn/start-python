"""
| - Binary OR operation
& - Binary AND operation
^ - Binary XOR operation
~ - Binary bitwise NOT operation
<< Left Shift operation
>> Right Shift operation
"""

num1 = 5 # 0101
num2 = 6 # 0110

#Binary OR
print (num1 | num2 ) # 0111

#Binary AND
print (num1 & num2)  # 0100

"""
XOR Rules
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""
#Binary XOR
print (num1 ^ num2)  # 0100

#Binary Bitwise Not Operation
print (~num1) # -num1 - 1

#Left Shift Operation
print (num1 << 3) # num << n → num * (2 ** n)

#Right Shift Operation
print (num1 >> 2) # num >> n → num // (2 ** n)