# Loops in Python> made new branch  
# Loops enable you to perform repetitive tasks efficiently without writing redundant code. They
# iterate over a sequence (like a list, tuple, string, or range) or execute a block of code as long as a
# specific condition is met.
# Types of Loops in Python
# 1. While loop
# 2. For loop
# 3. Nested loop

# While Loop
# The while loop repeatedly executes a block of code as long as a given condition remains
# True. It checks the condition before each iteration.

# for loop
# ====================
# The for loop is used when you know how many times you want to repeat something.
# Example:
# for i in range(5):
#     print("Hello", i)

# while loop
# ==============

# The while loop is used when you don’t know how many times it will run —
# it continues as long as the condition is True.
# Example:
# count = 1
# while count <= 5:
#     print("Count:", count)
#     count += 1

# Loop Control Statements:

# These help you manage how loops behave.

# break → Stops the loop completely
# ====================================
# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# continue → Skips the current iteration and goes to the next one
# ===============================================================
for i in range(5):
    if i == 2:
        continue
    print(i)
