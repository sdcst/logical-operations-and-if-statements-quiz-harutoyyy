"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
from math import sqrt

print("Input lengths of shorter triangle sides:")

a = float(input("a"))
b = float(input("b"))
hypotense = input(" One of the numbers is the hypotenuse of a right triangle? yes/no")
if hypotense in "yes":
    missingside = sqrt(a**2 + b**2)
    missingside = round(missingside,1)
    print(f"The length of missingside is {missingside}")
else:
    ("This is not the hypotenuse of a right triangle")