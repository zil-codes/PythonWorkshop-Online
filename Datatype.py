# What is a Data Type?
# -----------------------
# data types define the kind of value a variable can hold and how it can be used.
# every value stored in a variable has a type.
# That type tells what kind of data it is and what operations you can do with it.
# In short:
# Variable = box
# Data Type = label on the box that says what’s inside

# Numbers → int, float, complex
# Sequences → str, list, tuple
# Sets → set, frozenset
# Mapping → dict
# Boolean → bool
# Binary → bytes, bytearray, memoryview
# Special → None


# 1. Numeric Types
# -------------------------
# Used to store numbers.
# int → Integer numbers (positive, negative, zero)
# float → Decimal (floating-point) numbers
# complex → Numbers with real and imaginary parts
a = 10  # int
b = 3.14  # float
c = 2 + 5j  # complex

print (type(a))
print (type(b))
print (type(c))



# 2. Sequence Types
# ---------------------------------------------
# Ordered collections of items.
# str → String (text data)
# list → Ordered, mutable collection
# tuple → Ordered, immutable collection
# range → sequence of numbers


# text = "Hello"                # str
# name = "Zillur"               # String Formating
# age = 25
# city = "California"
# print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# numbers = ["you", "me", "mine"]        # list
# numbers[2] = "and her"                 # list mutable
# print (numbers)

# coordinates = (10, 20, 40)        # tuple
# coordinates [0] = (80)            # tuple not mutable
# print (coordinates)

# ran = range(10)                     # range
# print(ran)
# for x in ran:                      # for loop range to print 1 to10
#     print(x)


# Set Types
#--------------------------------------------
# Unordered collections of unique items.
# set → Mutable set of unique value
# frozenset → Immutable version of set
# s = {1, 2, 3, 4}              # set
# fs = frozenset([1, 2, 3])     # frozenset

# print(type(s))
# print(type(fs))

# Mapping Type
# ----------------------------------
# dict → Key-value pairs (like JSON objects)
# student = {"name": "Zillur", "age": 25, "city": "California"}

# print (student["name"])
# print(student["age"])
# print(student["city"])
# print(type(student))

# 5. Boolean Type
# ---------------------------------------
# Represents truth values.
# bool → True or False
# is_valid = True
# is_admin = False
# x = 8
# y = 10
# print (x > y)
# print(is_valid)
# print(is_admin)
# print(type(is_valid))

# Binary Types
# ------------------------------
# Used for raw binary data.
# bytes → Immutable sequence of bytes
# bytearray → Mutable sequence of bytes
# memoryview → Memory view of another binary object
# b = b"hello"             # bytes
# ba = bytearray([65, 66]) # bytearray
# mv = memoryview(b)       # memoryview
# print(b)
# print(ba)
# print(mv)


# 7. None Type
# ------------------------------------
# Represents the absence of a value.
# None → A special type with a single value
# x = None
# print(type(x))