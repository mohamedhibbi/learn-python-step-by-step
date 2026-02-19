# ======================================================
# If Statements
# Author: Mohamed Hibbi
# Description: Conditional tests, if/elif/else chains,
# checking items in lists, boolean values, and using
# if statements with lists.
# ======================================================

# -------------------------
# 1️⃣ A Simple Example - Conditional Logic
# -------------------------
# Special treatment for BMW - print it in uppercase

cars = ["bmw", "mercedes", "range rover", "audi", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# -------------------------
# 2️⃣ Conditional Tests
# -------------------------
# Conditional tests evaluate to True or False

# Equality comparisons
print(cars[0] == "bmw")       # True
print(cars[1] == "honda")     # False

# Case sensitivity matters!
print(cars[0] == "Bmw")       # False - case doesn't match
print(cars[0].title() == "Bmw")  # True - converted to title case first

# Inequality comparisons
print(cars[-1].lower() != "bugatti")  # True

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies")

# -------------------------
# 3️⃣ Numerical Comparisons
# -------------------------
# Compare numbers with ==, !=, <, >, <=, >=

age = 18
print(age == 18)  # True

answer = 17
if answer != 42:
    print(f"That's not the correct answer. Please Try Again!")

age = 19
print(age < 21)   # True
print(age <= 20)  # True
print(age > 21)   # False
print(age >= 21)  # False

# -------------------------
# 4️⃣ Using and & or - Multiple Conditions
# -------------------------
# and - BOTH conditions must be True
# or  - AT LEAST ONE condition must be True

age_0 = 22
age_1 = 18

# Using and - both must be True
if age_0 > 21 and age_1 > 21:
    print(f"Both people are over 21")  # Won't print

print(age_0 >= 21 and age_1 >= 21)  # False

# Parentheses for readability (optional but clear)
if (age_0 > 21) and (age_1 > 21):
    print("Both over 21")

# Using or - at least one must be True
if age_0 >= 21 or age_1 >= 21:
    print("At least one person is over 21")  # This prints!

# -------------------------
# 5️⃣ Checking if Items Are in a List
# -------------------------
# Use 'in' to check if an item exists in a list

requested_toppings = ["mushrooms", "onions", "eggplant"]
print("mushrooms" in requested_toppings)   # True
print("pepperoni" in requested_toppings)   # False

# Use 'not in' to check if an item does NOT exist
banned_users = ["andrew", "david", "johnny", "jimmy"]
user = "mohamed"
if user not in banned_users:
    print(f"{user.title()} is not banned")

# -------------------------
# 6️⃣ Boolean Values
# -------------------------
# Boolean values are simply True or False

game_active = True
can_edit = False

if game_active:
    print(f"The game is Already Active")
else:
    print(f"The game is Not Active")

# Using 'not' to negate a boolean
if not can_edit:
    print(f"You can't edit the game")
else:
    print(f"You can edit the game")

# -------------------------
# 7️⃣ Try It Yourself - Conditional Tests
# -------------------------
# Create 10 tests: 5 should be True, 5 should be False

cars = ["bmw", "mercedes", "bugatti", "toyota", "rolls royce", "DACIA"]

print(f"I Predict True")
print((cars[0] == "bmw"))

print(f"\nI Predict False")
print(cars[1] == "honda")

print(f"\nI Predict False")
print(cars[0] == "Bmw")

print(f"\nI predict True")
print(cars[0].upper() == "BMW")

print(f"\nI predict True")
print(cars[5].lower() == "dacia")

print(f"\nI predict False")
print("golf" in cars)

print(f"\nI predict True")
print("volk" not in cars)

# -------------------------
# 8️⃣ Simple if Statements
# -------------------------
# Runs code only if the condition is True

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# -------------------------
# 9️⃣ if-else Statements
# -------------------------
# Choose between two options

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print(f"Sorry, you are too young to vote!")
    print(f"Please register to vote as soon as you turn 18!")

# -------------------------
# 🔟 if-elif-else Chains
# -------------------------
# Handle multiple conditions in order
# Python stops at the first True condition

age = 12
if age < 4:
    print("Your Admission cost is: $0")
elif age < 18:
    print("Your Admission cost is: $5")
else:
    print("Your Admission cost is: $10")

# Cleaner version - store the price in a variable
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print(f"Your Admission Cost is: ${price}")

# Multiple elif blocks - seniors get a discount too!
age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5  # Senior discount
print(f"Your Admission Cost is: ${price}")

# -------------------------
# 1️⃣1️⃣ Using if Statements with Lists
# -------------------------
# Check for specific items in a list

requested_toppings = ["mushrooms", "extra cheese"]

# Check each topping individually
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")

print("\nFinished Making Your pizza!")

# -------------------------
# 1️⃣2️⃣ Try It Yourself - Alien Colors & Stages
# -------------------------

# Exercise 1: Alien Colors (Version 1 - Simple if)
alien_color = 'green'
if alien_color == 'green':
    earn = 5
print(f"Congratulations! You just earned {earn} points.")

# Exercise 1: Alien Colors (Version 2 - if-else)
alien_color = "red"
if alien_color == 'red':
    earn = 10
else:
    earn = 5
print(f"You earned {earn} points.")

alien_color = "black"
if alien_color == 'red':
    earn = 10
else:
    earn = 5
print(f"You earned {earn} points.")

# Exercise 1: Alien Colors (Version 3 - if-elif-else)
alien_color = "green"
if alien_color == 'green':
    earn = 5
elif alien_color == 'yellow':
    earn = 10
elif alien_color == 'red':
    earn = 15
print(f"You earned {earn} points.")

# Exercise 2: Stages of Life
age = 1
if age < 2:
    print("This person is a Baby!")
elif age < 4:
    print("This person is a toddler!")
elif age < 13:
    print("This person is a Kid!")
elif age < 20:
    print("This person is a Teenager!")
elif age < 65:
    print("This person is an Adult!")
elif age >= 65:
    print("This person is an Elder!")

# Exercise 3: Favorite Fruit
favorite_fruits = ["apple", "banana", "mango"]

if "banana" in favorite_fruits:
    print("You Really like banana!")
if "apple" in favorite_fruits:
    print("You Really like apple!")
if "mango" in favorite_fruits:
    print("You Really like mango!")
if "orange" in favorite_fruits:
    print("You Really like orange!")
if "cherry" in favorite_fruits:
    print("You Really like cherry!")

# -------------------------
# 1️⃣3️⃣ Summary - Quick Reference
# -------------------------
# | Statement Type    | When to Use                              |
# |-------------------|------------------------------------------|
# | if                | Run code only if condition is True       |
# | if-else           | Choose between two options               |
# | if-elif-else      | Handle multiple conditions in order      |
# | in                | Check if item exists in list             |
# | not in            | Check if item does NOT exist in list     |
# | and               | Both conditions must be True             |
# | or                | At least one condition must be True      |
# | ==                | Equal to                                 |
# | !=                | Not equal to                             |
# | <, >, <=, >=      | Less than, greater than, etc.            |

print("\n✅ All if statement exercises completed successfully!")
