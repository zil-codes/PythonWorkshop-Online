
# Functions
# =======================
# A function is a block of code that performs a specific task. You can use it whenever you want
# by calling its name, which saves you from writing the same code multiple times.
# Benefits of Using Function: Increases code Readability & Reusability.

# Basic Concepts:
# *   Create function: Use the def keyword to define a function.
# *   Call function: Use the function's name followed by () to run it
# *   Parameter: The variable listed inside parentheses in function definition
# *   Argument: The actual value you pass to function when you call it

# Types of Functions
# ==========================
# Below are the two types of functions in Python:
# 1. Built-in library function:
# *   These are Standard functions in Python that are available to use.
# *   Examples: print(), input(), type(), sum(), max), etc
# 2. User-defined function:
# *   We can create our own functions based on our requirer
# *   Examples: create your own function :)

#create function without parameter
# =========================================
def greetings():
    print("Welcome to the python course")

#call function (use function)
greetings()

#create function with parameter
# =========================================
# def add (a, b):
#     result = a + b
#     print ("the sum is", result)
# add (5,3)


# The return Statement
# =============================
# The return statement is used in a function to send a result back to the place
# where the function was called. When return is executed, the function stops
# running and immediately returns the specified value.

# Example:
# def add(a, b):
#   return a + b # This line sends back sum of a and b
# result = add(3, 5)
# print(result)

# The pass Statement
# ====================================
# The pass statement is a placeholder in a function or loop. It does nothing and is
# used when you need to write code that will be added later or to define an empty function.
# Example:
# def myfunction():
# pass # This does nothing for now

# Create a sample calculator
# ===========================

# Write a Python program to create a calculator that can perform at least five
# different mathematical operations such as addition, subtraction, multiplication,
# division and average. Ensure that the program is user-friendly, prompting for input
# and displaying the results clearly.

# 1. function for operators
# 2. User input
# 3. print result

# 1. function for operators
# Function to add two numbers
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def avg(num1, num2):
    return (num1 + num2)/2

# 2. User input
print ("please select an operation: \n" \
       "1) Add \n" 
       "2) Subtract \n"
       "3) Multiply \n" 
       "4) Divide \n"
       "5) Average \n")

select = int(input("Select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# 3. print result
if select == 1:
    print (number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print (number1,"-", number2, "=", sub(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", mult(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", div(number1, number2))
elif select == 5:
    print("(", number1, "+", number2,")", "2", "=", avg(number1, number2))
else:
    print("invalid operation Please select again")



