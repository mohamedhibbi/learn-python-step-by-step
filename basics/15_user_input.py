# ======================================================
# User Input and int()
# Author: Mohamed Hibbi
# Description: Using input() to get user input,
# converting input to numbers with int(),
# and using the modulo operator %.
# ======================================================

# -------------------------
# 4️⃣0️⃣ Getting Input With input()
# -------------------------
# input() pauses the program and waits for the user to type something
# Whatever the user types is stored as a string in the variable
# The text inside input() is the prompt — what the user sees

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# -------------------------
# 4️⃣1️⃣ Writing Clear Prompts
# -------------------------
# Use += to build a multi-line prompt for better readability
# This keeps your code clean when the prompt is long

prompt = "If you tell us who you are, we can personalize the message you see"
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name}!")

# -------------------------
# 4️⃣2️⃣ Using int() to Convert Input to a Number
# -------------------------
# input() always returns a string — even if the user types a number
# Use int() to convert it so you can do math with it
# You can convert on the same line or store first then convert

# One line approach
age = int(input("What's your age? "))
age_of_birth = 2026 - age
print(f"Your year of birth is {age_of_birth}")

# -------------------------
# 4️⃣3️⃣ Combining int() With if Statements
# -------------------------
# Once converted to an integer, you can use it in conditions

height = int(input("How tall are you <in centimeters>? "))
if height >= 170:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# -------------------------
# 4️⃣4️⃣ The Modulo Operator %
# -------------------------
# % gives you the remainder after division
# If the remainder is 0, the number divides evenly
# Most common use: checking if a number is even or odd
#
# Examples:
# 4 % 2 = 0  → even
# 5 % 2 = 1  → odd
# 10 % 10 = 0 → multiple of 10

number = input("Enter a number and I will tell you if it's an even or odd number: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")

# -------------------------
# 4️⃣5️⃣ Try It Yourself - Rental Car, Restaurant & Multiple of Ten
# -------------------------

# Exercise 7-1: Rental Car
car_name = input("What's the name of your favorite car: ")
car_name = car_name.title()
print(f"\n{car_name} is such an amazing car")

# Exercise 7-2: Restaurant Seating
message = input("How many people are in your dinner group? ")
message = int(message)
if message > 8:
    print("Sorry! You'll have to wait for a table.")
else:
    print("Your table is ready!")

# Exercise 7-3: Multiple of Ten
number = input("Enter a number and I will tell you if it's a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10")
else:
    print(f"The number {number} is not a multiple of 10")

# -------------------------
# 4️⃣6️⃣ Summary - Quick Reference
# -------------------------
# | Concept                  | Syntax / Example                        |
# |--------------------------|------------------------------------------|
# | Get user input           | name = input("What is your name? ")     |
# | Multi-line prompt        | prompt = "..."; prompt += "\n..."       |
# | Convert to integer       | age = int(input("Your age? "))          |
# | Convert after storing    | number = input(); number = int(number)  |
# | Modulo operator          | 10 % 3 → 1 (remainder)                 |
# | Check even/odd           | if number % 2 == 0: → even              |
# | Check multiple           | if number % 10 == 0: → multiple of 10  |

print("\n✅ All user input exercises completed successfully!")
