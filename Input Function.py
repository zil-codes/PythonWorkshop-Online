# INPUT FUNCTION
# ==================================
# The input function is an essential feature in Python that allows to take input from the user.
# This is particularly useful when you want to create interactive programs where the user
# can provide data during execution.
# How the input Function Works:
# ==================================
# The input function waits for the user to type something and then press Enter.
# It reads the input as a string and returns it. Example:
# Prompting the user for their name

# name = input("Enter your name: ")
# print(name)
# print (f"welcome {name} to python tutorial") # With an f-string, you can embed variables or
                                              # expressions directly inside { } within the string,
                                              # and Python will replace them with their values.

# age = int(input("Enter your age: "))
#  print(age)
# print (f"so next year you wiil be {int(age)+1} ")

# answer =input ("reply:")
# print (answer)

# multple input from user
# input from user to add two number and print result
# x = input("Enter first number: ")
# y = input("Enter second number: ")
#
# print(f"Sum of {x} & {y} is {int(x) + int(y)}")


# PRACTICE 1
# ============================
# Write a Python program to input student name and marks of 3 subjects.
# Print name & Percentage in output.

student_name = input("Enter student name: ")
english = int(input ("enter english mark: "))
math = int(input("enter math mark: "))
science = int(input ("enter science mark: "))

# calculate percentage
percentage = ((english + math + science)/300)*100
# each subject mark 100 so 3*100=300 then *100
print (f"the result of {student_name} is {int(percentage)}%. good")

# PRACTICE 2
# ============================
# Write a Python program that collects multiple types of data
# (e.g., name, age, height, and student status) from user input,
# stores them in a dictionary, and then prints out the collected data?

