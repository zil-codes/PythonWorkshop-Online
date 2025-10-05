# What are Operators? Create new branch
# ==============================================
# Operators are special symbols in Python that perform operations on values (operands).
# x = 10
# y = 3
# print(x + y)   # 13  (here `+` is an operator)

# Types of Operators in Python
# ===============================================
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators


# 1. Arithmetic Operators (Math operations)
# ===============================================
# x = 10
# y = 3
#
# print(x + y)   # 13  (Addition)
# print(x - y)   # 7   (Subtraction)
# print(x * y)   # 30  (Multiplication)
# print(x / y)   # 3.333... (Division → float)
# print(x // y)  # 3   (Floor Division → integer result)
# print(x % y)   # 1   (Modulus → remainder)
# print(x ** y)  # 1000 (Exponent → 10^3)

# 2. Assignment Operators
# ===============================================
# Used to assign values to variables
# x = 5
# x += 3   # x = x + 3 → 8
# x -= 2   # x = x - 2 → 6
# x *= 4   # x = x * 4 → 24
# x /= 3   # x = x / 3 → 8.0
# x %= 5   # x = x % 5 → 3.0
# x **= 2  # x = x ** 2 → 9.0
# x //= 2  # x = x // 2 → 4.0


# 3. Comparison (Relational) Operators
# ================================================
# Used to compare values → result is True/False

# a = 5
# b = 10

# print(a == b)  # False  (equal)
# print(a != b)  # True   (not equal)
# print(a > b)   # False
# print(a < b)   # True
# print(a >= 5)  # True
# print(b <= 5)  # False

# 4. Logical Operators
# =================================================
# Used with conditions
# Rules
# True + True = True
# True + False = False
# false + False = False

# x = True
# y = False

# Rule for "and" operator True + True = True/ True + False = False/ false + False = False
# print(x and y)  # False (Both must be True)
# print  (x==True and y==False)

# Rule for "or" operator True + False = True
# print(x or y)   # True  (At least one True)

# print(not x)    # False (Opposite of x)
# print (not (x==True and y==False))

# 5. Identity Operators
# =====================================================
# Compare if two variables are the same object in memory

x = [1, 2, 3]
y = x
z = [1, 2, 3]

# print(x is y)      # True (values are equal) is operator
# print(x is z)      # False (different objects with same values)
# print(x is not z)      # True  (same object in memory) is not operator

# 6. Membership Operators
# ====================================================
# Check if a value is inside a sequence (string, list, tuple, etc.) in, not in

# numbers = [1, 2, 3, 4, 5]
# print(3 in numbers)     # True
# print(10 not in numbers) # True


# 5. Bitwise Operators
# =====================================================
# Work at the binary level

# a = 5   # (5 in binary- 0101, 0 =false and 1 true)
# b = 3   # (3 in binary- 0011)
# print (a & b) # (1 in binary- 0001)
# Rule for "&" operator True + True = True/ True + False = False/ false + False = False

# print(a & b)   # 2  (AND → 010)
# print(a | b)   # 7  (OR → 111)
# print(a ^ b)   # 5  (XOR → 101)
# print(~a)      # -7 (NOT → inverts bits)
# print(a << 1)  # 12 (Left shift → 1100)
# print(a >> 1)  # 3  (Right shift → 011)
