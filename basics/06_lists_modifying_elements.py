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
for guest in names:
    print(f"Hello {guest.title()}! I would like to invite you to dinner.")

# Replacement for absent guest
absent = names.pop(2).title()  # othman can't make it
print(f"{absent} can't make it to dinner.")

names.insert(2, "mohamed")  # replacement
print(f"The replacement of Othman is {names[2]}.")

# Updated invitations
for guest in names:
    print(f"Hello {guest.title()}! I would like to invite you to dinner.")

# Adding more guests
names.insert(0, "khabab")
names.insert(2, "zaid")
names.append("abu obaida")  # simpler than using exact index

# Invitations to all guests
print("\nUpdated invitations to all guests:")
for guest in names:
    print(f"Hello {guest.title()}! I would like to invite you to dinner.")

# -------------------------
# 6️⃣ Summary
# -------------------------
print("\n✅ All list exercises completed successfully!")

