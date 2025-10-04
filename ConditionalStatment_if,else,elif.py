
# Conditional Statement
# ============================================
# Conditional statements allow you to execute code based on condition evaluates
# to True or False. They are essential for controlling the flow of a program and
# making decisions based on different inputs or conditions.

# ' if' Conditional Statement
# =========================================
# The if statement is used to test a condition and execute a block of code only if the condition is true.

# Syntax
# if condition:
# # Code to execute if the condition is true

# Example
# age = 26
# if age > 19:
#     print("You are an adult")


# 'if-else' Conditional Statement
# ===========================================
# The if-else statement provides an alternative block of code to execute if the condition is false.

# Syntax
# Example
# if condition:
# Code to execute if the condition is true

# else:
# Code to execute if the condition is false
# temperature = 30
# if temperature > 25:
#     print("It's a hot day.")
# else:
#     print("It's a cool day.")

# 'if-elif-else' Conditional Statement
# =======================================
# The if-elif-else statement allows to check multiple conditions and execute
# different blocks of code based on which condition is true.
# Syntax
# if condition1:
# # Code to execute if condition is true
# elif condition2:
# # Code to execute if condition is true
# else:
# Code to execute if none of the above conditions are true

# 'if-elif-else' Conditional Statement
# Grading system: Let's write a code to classify the student's grade based on their total marks (out of hundred).
# Example
#
# marks = int(input("Enter marks-100: "))
# if marks >= 90:           #  >= greater than or equal
# 	print ("Grade  A")
# elif marks >= 80:
# 	print( "Grade B")
# elif marks >=70:
# 	print ("Grade C")
# else:
# 	print ("Grade  D")

# Nested 'if-else' Conditional Statement
# =============================================
# A nested if-else statement in Python involves placing an if-else statement
# inside another if-else statement. This allows for more complex decision-making
# by checking multiple conditions that depend on each other.

# Syntax:
# if condition1:
    # Code block for condition1 being True
    # if condition2:
    # Code block for condition2 being True
    # else:
    # Code block for condition2 being False
# else:
# Code block for condition1 being False

# username = "admin"
# password = "Test124"

# if username == "admin":
#     if password == "Test124":
#         print("Login Successful ✅")
#     else:
#         print("Wrong Password ❌")
# else:
#     print("User not found ❌")

# Conditional Expressions
# =======================================
# Conditional expressions provide a shorthand way to write simple if-else statements.
# Also known as Ternary Operator.
# Syntax
# value_if_true if condition else value_ if_false

# Example
# age = 26
# status = "Adult" if age >= 18 else "Child"
# print(status)

# value = None
#
# if value:
#     print("the value is true")
# else:
#     print("the value is false")

# write a simple program to determine if a given year is a leap year using user input

