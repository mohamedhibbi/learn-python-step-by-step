# ======================================================
# Working With Lists - Numerical Lists & Slicing
# Author: Mohamed Hibbi
# simple statistics, slicing lists, and copying lists
# Description: Using range(), list comprehensions,.
# ======================================================

# -------------------------
# 1️⃣ Using range()
# -------------------------
# range() generates a sequence of numbers
# range(start, stop) → stops BEFORE the stop value

numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# -------------------------
# 2️⃣ Using range() with a Step Value
# -------------------------
# range(start, stop, step) → skips by the step value

even_numbers = list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
print(even_numbers)

# -------------------------
# 3️⃣ Building a List with a Loop
# -------------------------
# Traditional way: empty list + loop + append

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# -------------------------
# 4️⃣ Simple Statistics with Number Lists
# -------------------------
# min(), max(), sum() work on any list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 0
print(max(digits))  # 9
print(sum(digits))  # 45

# Edge case: range() starts at 0 by default
nums = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
print(max(nums))  # 9

# -------------------------
# 5️⃣ List Comprehensions
# -------------------------
# Write the entire loop in ONE line!
# Pattern: [expression for item in iterable]

squares = [value**2 for value in range(1, 11)]
print(squares)  # Same result as the loop version above!

# More examples
even_numbers = [number for number in range(2, 21, 2)]
print(even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_numbers = [number for number in range(1, 21, 2)]
print(odd_numbers)   # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# -------------------------
# 6️⃣ Try It Yourself — Numerical Lists
# -------------------------

# Exercise 1: Counting to Twenty
numbers = list(range(1, 21))
for number in numbers:
    print(number)

# Exercise 2: One Million
numbers = list(range(1, 1000001))
# for number in numbers:
#     print(number)  # Too many to print! But works.
print(min(numbers))    # 1
print(max(numbers))    # 1000000
print(sum(numbers))    # 500000500000

# Exercise 3: Odd Numbers (corrected)
odd_numbers = list(range(1, 21, 2))  # ✅ Starts at 1, not 2
for odd_number in odd_numbers:
    print(odd_number)

# Exercise 4: Threes
multiples = list(range(3, 31, 3))
for multiple in multiples:
    print(multiple)

# Exercise 5: Cubes (both ways)
cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

# List comprehension version
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

# -------------------------
# 7️⃣ Slicing a List
# -------------------------
# Slice syntax: list[start:stop]
# Stops BEFORE the stop index (just like range)

names = ["mohamed", "sara", "hanae", "max", "mimi"]
print(names[0:3])   # ['mohamed', 'sara', 'hanae']
print(names[1:4])   # ['sara', 'hanae', 'max']
print(names[:4])    # first 4 (start = 0 by default)
print(names[2:])    # from index 2 to end
print(names[-3:])   # last 3 items

# Looping through a slice
print("Here are the first three players on my team:")
for name in names[:3]:
    print(name.title())

# -------------------------
# 8️⃣ Copying a List
# -------------------------
# ✅ CORRECT way: use [:] to create a copy
# ❌ WRONG way: assignment (both point to same list)

my_foods = ["tagine", "pizza", "chiken", "falafel"]
friend_foods = my_foods[:]  # ✅ Creates a NEW list

print(f"\nMy Friend's favorite foods are:")
print(f"\t{friend_foods}")

# Prove they're independent by adding different items
my_foods.append("eggs")
friend_foods.append("oats")

print(my_foods)      # has "eggs"
print(friend_foods)  # has "oats"

# ❌ What happens WITHOUT [:] (wrong way):
# friend_foods = my_foods  # Both point to SAME list!
# my_foods.append("eggs")
# print(friend_foods)  # also has "eggs" — they're the same!

# -------------------------
# 9️⃣ Try It Yourself — Slicing & Copying
# -------------------------

# Exercise 1: Slices
players = ["messi", "neymar", "cristiano", "hazard", "ramos", "suarez", "ronaldo"]
print(f"The first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[2:5]}")
print(f"The last three items in the list are: {players[-3:]}")

# Exercise 2: My Pizzas, Your Pizzas
my_pizzas = ["margherita", "pepperoni", "hawaiian"]
friend_pizzas = my_pizzas[:]  # ✅ Proper copy

print(f"My Favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

friend_pizzas.append("chiken")
print(f"\nMy Friend's Favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# -------------------------
# 🔟 Summary — Quick Reference
# -------------------------
# | Function/Method        | Description                          |
# |------------------------|--------------------------------------|
# | range(start, stop)     | Generate numbers from start to stop-1|
# | range(start, stop, step)| Skip by step value                  |
# | list(range(...))       | Convert range to actual list         |
# | min(list)              | Find smallest value                  |
# | max(list)              | Find largest value                   |
# | sum(list)              | Add all values together              |
# | [expr for x in list]   | List comprehension (one-line loop)   |
# | list[start:stop]       | Slice from start to stop-1           |
# | list[:n]               | First n items                        |
# | list[n:]               | From n to end                        |
# | list[-n:]              | Last n items                         |
# | list[:]                | Copy the entire list ✅              |

print("\n✅ All numerical lists and slicing exercises completed successfully!")
