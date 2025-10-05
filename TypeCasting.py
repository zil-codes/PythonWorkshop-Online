# What is Type Casting= branch
# Type casting in Python refers to the process of converting a value from one data type to another.
# This can be useful in various situations, such as when you need to perform operations
# between different types or when you need to format data in a specific way.
# Python has several built-in functions for type casting:
# =========================================================
# int(): Converts a value to an integer.
# float(): Converts a value to a floating-point
# str: Converts a value to a string.
# List, tuple(), set(), dict() and bool()

# int(): Converts a value to an integer.
# a = 1
# print (type(a))
# b = "1"
# print (type(b))
# c = int(b)
# print (type(c))
#
# print (a+c)
# print(a+int(b)) # another way

# str: Converts a value to a string.
# num = 12
# num2 = str(num)
# print (type(num2))

# float(): Converts a value to a floating-point
# z1 = 23
# z2 = float(z1)
# print (type(z2))

# IMPLICIT TYPE CASTING
# =================================
# Also known as coercion, is performed automatically by the Python interpreter.
# This usually occurs when performing operations between different data types,
# and Python implicitly converts one data type to another to avoid data loss or errors.

# Implicit type casting from integer to float
# num_int = 10
# num_float = 5.5
# result = (num_int + num_float)
# print(result)

# EXPLICIT TYPE CASTING
# Also known as type conversion, is performed manually by the programmer using built-in functions.
# This is done to ensure the desired type conversion and to avoid unexpected behavior.
# Converting String to Integer:
# str_num = "26"
# int_num = int(str_num)
# print(int_num)
# print(type(int_num))

# # Converting a value to boolean:
x0 = bool (0)
print (x0)
print (type(x0))

x1 = bool (1)
print (x1)
print (type(x1))
