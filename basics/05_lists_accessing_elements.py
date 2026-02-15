"""
05 - Lists: Accessing Elements

This lesson covers:
1. Creating a list
2. Accessing elements using index
3. Understanding zero-based indexing
4. Using list values inside f-strings
5. Applying string methods on list elements
"""

# -----------------------------------
# 1️⃣ Creating a List
# -----------------------------------

names = ["karim", "abdo", "omar", "ali", "hamza", "saad", "khabab"]

# Lists are ordered collections.
# Each element has an index.
# IMPORTANT: Indexing starts at 0 (zero-based indexing).

print("\n--- Accessing List Elements ---")

print(f"First name in the list is {names[0]}")
print(f"Second name in the list is {names[1]}")
print(f"Third name in the list is {names[2]}")

# -----------------------------------
# 2️⃣ Creating Greeting Messages
# -----------------------------------

print("\n--- Greeting Messages ---")

print(f"Hello {names[0].title()}, nice to have you as a friend.")
print(f"Hello {names[1].title()}, nice to have you as a friend.")
print(f"Hello {names[2].title()}, nice to have you as a friend.")

# -----------------------------------
# 3️⃣ Another Example with Cars
# -----------------------------------

cars = ["mercedes", "rolls royce", "bugatti", "bmw"]

print("\n--- Using String Methods on List Elements ---")

print(f"I would like to own a {cars[0].title()}")
print(f"I would like to own a {cars[3].upper()}")
print(f"I would like to own a {cars[2].capitalize()}")


# -----------------------------------
# 🧠 Key Concepts
# -----------------------------------
# - Lists use square brackets []
# - Indexing starts at 0
# - You can apply string methods directly to list elements
# - Lists are mutable (we will explore that later)

