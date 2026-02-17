# ======================================================
# List Exercises in Python
# Author: Mohamed
# Description: Examples of creating, modifying, inserting,
# removing elements in lists, and working with strings.
# ======================================================

# -------------------------
# 1️⃣ Creating and modifying lists
# -------------------------
cars = ["mercedes", "bmw", "honda"]
print("Original cars list:", cars)

# Update an element
cars[2] = "bugatti"
print("After updating:", cars)

# Add a new element
cars.append("rolls royce")
print("After appending:", cars)

# -------------------------
# 2️⃣ Adding items to an empty list
# -------------------------
players = []
players.append("messi")
players.append("batman")
players.append("spiderman")
print("Players list:", players)

# -------------------------
# 3️⃣ Inserting elements
# -------------------------
names = ["abubakr", "omar"]
names.insert(2, "othman")
names.insert(3, "ali")
names.insert(0, "mohamed")
print("Names list after inserts:", names)

# -------------------------
# 4️⃣ Removing elements
# -------------------------
# Using del
del players[1]  # removes "batman"
print("Players after del:", players)

# Using pop()
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last owned motorcycle is {last_owned.title()}")
print("Motorcycles after pop:", motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first owned motorcycle is {first_owned.title()}")
print("Motorcycles after popping first:", motorcycles)

# Using remove()
fruits = ["apple", "banana", "cherry", "carrot"]
not_fruit = "carrot"
fruits.remove(not_fruit)
print("Fruits after removing non-fruit:", fruits)
print(f"A {not_fruit} is not a fruit, so I removed it from the list.")

# -------------------------
# 5️⃣ Dinner invitation example
# -------------------------
names = ["abubakr", "omar", "othman", "ali"]

# Initial invitations
print(f"Hello {names[0].title()}! I would like to invite You to Dinner")
print(f"Hello {names[1].title()}! I would like to invite You to Dinner")
print(f"Hello {names[2].title()}! I would like to invite You to Dinner")
print(f"Hello {names[3].title()}! I would like to invite You to Dinner")

# Othman can't make the dinner
absent = names.pop(2).title()
print(f"{absent} can't make it to dinner")
names.insert(2, "mohamed")
print(f"The replacement of Othman is {names[2]}")

# Updated invitations
print(f"Hello {names[0].title()}! I would like to invite You to Dinner")
print(f"Hello {names[1].title()}! I would like to invite You to Dinner")
print(f"Hello {names[2].title()}! I would like to invite You to Dinner")
print(f"Hello {names[3].title()}! I would like to invite You to Dinner")

# More guests to add
names.insert(0, "khabab")
names.insert(2, "zaid")
names.insert(6, "abu obaida")

# Invitations to all guests
print(f"Hello {names[0].title()}! I would like to invite You to Dinner")
print(f"Hello {names[1].title()}! I would like to invite You to Dinner")
print(f"Hello {names[2].title()}! I would like to invite You to Dinner")
print(f"Hello {names[3].title()}! I would like to invite You to Dinner")
print(f"Hello {names[4].title()}! I would like to invite You to Dinner")
print(f"Hello {names[5].title()}! I would like to invite You to Dinner")  
print(f"Hello {names[6].title()}! I would like to invite You to Dinner")

# Shrinking guest list
print(f"\nI only can invite two people")
name1 = names.pop(6)
print(f"Sorry {name1.title()}! I Can't Invite you to dinner, I only have space for two people")
name2 = names.pop(5)
print(f"Sorry {name2.title()}! I Can't Invite you to dinner, I only have space for two people")
name3 = names.pop(4)
print(f"Sorry {name3.title()}! I Can't Invite you to dinner, I only have space for two people")
name4 = names.pop(3)
print(f"Sorry {name4.title()}! I Can't Invite you to dinner, I only have space for two people")
name5 = names.pop(2)
print(f"Sorry {name5.title()}! I Can't Invite you to dinner, I only have space for two people")

del names[0:]
print(names)

# -------------------------
# 6️⃣ Summary
# -------------------------
print("\n✅ All list exercises completed successfully!")
