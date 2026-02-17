# ======================================================
# Working With Lists - For Loops & Indentation
# Author: Mohamed Hibbi
# Description: Examples of looping through lists,
# doing more work within loops, avoiding indentation
# errors, and forgetting the colon.
# ======================================================

# -------------------------
# 1️⃣ Looping Through a List
# -------------------------
# Instead of printing each item manually,
# a for loop does it automatically for every item!

names = ["mohamed", "sara", "hanae", "max", "mimi"]
for name in names:
    print(name)

# The variable "name" is our choice — it holds each
# item one at a time as the loop goes through the list

# -------------------------
# 2️⃣ Doing More Work Within a for Loop
# -------------------------
# Every INDENTED line runs for EVERY item in the list
# Just like YAML — indentation defines what belongs to what!

names = ["mohamed", "sara", "hanae", "max", "mimi"]
for name in names:
    print(f"{name.title()}, Love having you as a Family Member!")
    print(f"\t{name.title()} Love You!\n")

# -------------------------
# 3️⃣ Doing Something After a for Loop
# -------------------------
# Lines OUTSIDE the loop (no indent) run only ONCE
# after all items have been processed

names = ["mohamed", "sara", "hanae", "max", "mimi"]
for name in names:
    print(f"Hello {name.title()}!")         # runs for EVERY name
    print(f"I love you {name.title()}!\n")  # runs for EVERY name

print("Done! That's all the names.")        # runs ONCE at the end

# -------------------------
# 4️⃣ Avoiding Indentation Errors
# -------------------------

# ❌ MISTAKE 1: Unnecessarily Indenting a Line
# Indenting a line that doesn't belong to any loop
# causes an IndentationError

message = "what a Good day to learn Python!"
#    print(message)  # ❌ IndentationError: unexpected indent
print(message)        # ✅ correct — no unnecessary indent

# ❌ MISTAKE 2: Forgetting to Indent Inside a Loop
# If you forget to indent inside a loop,
# Python won't know the line belongs to the loop

# ❌ MISTAKE 3: Accidentally Indenting After the Loop
# This is a logic error — Python won't crash
# but the output won't be what you expected!

names = ["mohamed", "sara", "hanae", "max", "mimi"]
for name in names:
    print(f"Hello {name.title()}!")
    print(f"I love you {name.title()}!")
    print("Done! That's all the names.")  # ❌ inside loop — runs 5 times!
    print("hello\n")

# ✅ Correct version — "Done!" outside the loop
for name in names:
    print(f"Hello {name.title()}!")
    print(f"I love you {name.title()}!\n")

print("Done! That's all the names.")      # ✅ outside loop — runs ONCE

# -------------------------
# 5️⃣ Forgetting the Colon
# -------------------------
# The colon at the end of a for statement is required!
# Without it Python throws a SyntaxError immediately

# ❌ Missing colon:
# for name in names    # SyntaxError: expected ':'
#     print(name)

# ✅ Correct:
for name in names:     # colon tells Python "loop definition done, start the block"
    print(name)

# TIP: PyCharm and VS Code underline this error instantly
# before you even run the code — hover over the red line
# to see what's wrong!

# -------------------------
# 6️⃣ Try It Yourself — Pizzas & Animals
# -------------------------

# 🍕 Exercise 1: Pizzas
pizzas = ["margherita", "pepperoni", "bbq chicken", "four cheese", "hawaiian"]
for pizza in pizzas:
    print(f"I Like {pizza.title()} pizza!\n")
print("\tI really Love Pizza!")

# 🐾 Exercise 2: Animals
animals = ["dog", "cat", "lion"]
for animal in animals:
    print(f"A {animal.title()} Would Make a great pet!")
print("\nAny of these animals would make a great pet!")

# -------------------------
# 7️⃣ Summary — Indentation Rules Cheat Sheet
# -------------------------
# | Situation                        | Result                        |
# |----------------------------------|-------------------------------|
# | Line indented inside loop        | Runs once per item ✅         |
# | Line not indented outside loop   | Runs once total ✅            |
# | Line indented with nothing above | IndentationError ❌           |
# | Missing colon after for          | SyntaxError ❌                |
# | Accidentally indented after loop | Logic error - runs too many times ⚠️ |
# | name after loop ends             | Holds last value from loop ⚠️ |

print("\n✅ All for loop and indentation exercises completed successfully!")
