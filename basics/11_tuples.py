# ======================================================
# Working With Lists - Tuples
# Author: Mohamed Hibbi
# Description: Understanding immutable lists (tuples),
# how to define them, loop through them, and the
# difference between tuples and lists.
# ======================================================

# -------------------------
# 1️⃣ What is a Tuple?
# -------------------------
# A tuple is like a list, but IMMUTABLE — you can't change it
# after creation. Use parentheses () instead of brackets []

# Lists use []
my_list = [200, 50]
my_list[0] = 300  # ✅ Lists CAN be modified

# Tuples use ()
dimensions = (200, 50)
# dimensions[0] = 300  # ❌ TypeError: tuples CANNOT be modified

# -------------------------
# 2️⃣ Defining and Accessing Tuples
# -------------------------
# Access items the same way as lists — using indices

dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# -------------------------
# 3️⃣ Tuples Are Immutable
# -------------------------
# Once created, you CANNOT change individual items

dimensions = (200, 50)
# dimensions[0] = 300  # ❌ TypeError: 'tuple' object does not support item assignment
print(dimensions[0])

# This is useful when you have data that should NEVER change:
# - Screen dimensions
# - RGB color values
# - Geographic coordinates
# - Constants in your program

# -------------------------
# 4️⃣ Looping Through a Tuple
# -------------------------
# Just like lists, you can loop through tuples with for loops

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# -------------------------
# 5️⃣ Overwriting a Tuple
# -------------------------
# While you can't modify individual items,
# you CAN reassign the entire variable to a NEW tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Reassign to a completely new tuple
dimensions = (300, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# What's happening here:
# - The original (200, 50) tuple is discarded
# - A new (300, 100) tuple is created
# - The variable 'dimensions' now points to the new tuple

# -------------------------
# 6️⃣ Try It Yourself — Buffet
# -------------------------
# A restaurant offers a buffet with basic foods that don't change

simple_foods = ("rice", "bread", "eggs", "milk", "apple")

print("Original menu:")
for simple_food in simple_foods:
    print(simple_food)

# Try to modify one item (this will fail!)
# simple_foods[0] = "banana"  # ❌ TypeError: 'tuple' object does not support item assignment

# Restaurant changes the menu — replace the entire tuple
simple_foods = ("rice", "bread", "eggs", "banana", "orange")

print("\nRevised menu:")
for simple_food in simple_foods:
    print(simple_food)

# -------------------------
# 7️⃣ Lists vs Tuples — When to Use Which?
# -------------------------
# | Feature          | List []           | Tuple ()          |
# |------------------|-------------------|-------------------|
# | Mutable?         | ✅ Yes            | ❌ No             |
# | Syntax           | [1, 2, 3]         | (1, 2, 3)         |
# | Can modify items | ✅ Yes            | ❌ No             |
# | Performance      | Slower            | Faster            |
# | Use when...      | Data will change  | Data is constant  |

# Examples:
# Use LISTS for: shopping cart, to-do list, player scores
# Use TUPLES for: RGB colors, screen size, date of birth

# -------------------------
# 8️⃣ Summary — Quick Reference
# -------------------------
# Defining a tuple:
my_tuple = (10, 20, 30)

# Accessing items:
print(my_tuple[0])  # 10

# Looping:
for item in my_tuple:
    print(item)

# Can't modify:
# my_tuple[0] = 100  # ❌ TypeError

# Can overwrite entire tuple:
my_tuple = (100, 200, 300)  # ✅ Works

print("\n✅ All tuple exercises completed successfully!")
