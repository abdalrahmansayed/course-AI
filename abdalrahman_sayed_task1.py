# -*- coding: utf-8 -*-
"""abdalrahman sayed - task1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VddfrnPWVHRDMAQt99iazh1uXKnXWIrq

## **1- Write a Python program to find the area of a triangle**
"""

# Program to find the area of a triangle

# Input base and height from the user
base = float(input("Enter the base:"))
height = float(input("Enter the height:"))

# Calculate the area
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle is: {area}")

"""# **2- Write a Python program to swap two variables.**

"""

# Input two numbers
a = input("num1:")
b = input("num2:")

# Swap
x = a
a = b
b = x

print(f"After swapping: a = {a}, b = {b}")

"""# **3-Write a Python program to enter a number from user and convert this number from kilometers to miles.**

"""

# Get input from the user
kilometers = float(input("Enter the distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Convert kilometers to miles
miles = kilometers * conversion_factor

# Display the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")