import math #imports a certain library which allows new functions and constants using dots

result = math.sqrt(25) #sqrt stands for square root which isnt a built in function in python itself
print(result) #We are able to access it though due to importing the library and all of its new functions along with it


from math import sqrt, pi #takes certain functions from a certain library and only allows those specific functions

result1 = sqrt(16) 
print(result1)
print(pi)


import math as mt #replaces the name math with mt for using functions to your preference

math_example = mt.array([1, 2, 3]) #Example