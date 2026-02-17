# ======================================================
# Avoiding Index Errors When Working With Lists
# Author: Mohamed Hibbi
# Description: Understanding IndexError, how it happens,
# how to avoid it, and how to debug it when it occurs.
# ======================================================

# -------------------------
# 1️⃣ What is an IndexError?
# -------------------------
# An IndexError occurs when you try to access an index
# that doesn't exist in the list.
# Remember: a list with 5 items has indices 0 to 4 — NOT 5!

names = ["mohamed", "sara", "hanae", "max", "mimi"]
# print(names[5])  # ❌ IndexError: list index out of range
                   # There is no 6th item — index 5 doesn't exist!

# -------------------------
# 2️⃣ Safely Accessing the Last Item with -1
# -------------------------
# Instead of calculating the last index manually,
# use -1 to always get the last item in any list

names = ["mohamed", "sara", "hanae", "max", "mimi"]
print(names[-1])   # ✅ returns "mimi" — the last item
print(names[-2])   # ✅ returns "max" — second to last

# This is especially useful when you don't know
# how long the list is!

# -------------------------
# 3️⃣ The Empty List Trap
# -------------------------
# The ONLY time -1 will cause an IndexError is
# when the list is completely empty

names = []
# print(names[-1])  # ❌ IndexError: list index out of range
                    # There are no items at all — not even a last one!

# -------------------------
# 4️⃣ How to Debug an IndexError
# -------------------------
# If an IndexError occurs and you can't figure out
# how to resolve it, try:
# 1. Printing the list to see its actual contents
# 2. Printing len() to see how many items it has
# It will likely look much different than you thought!

names = ["mohamed", "sara", "hanae", "max", "mimi"]
print(f"List contents: {names}")       # see what's actually in the list
print(f"List length: {len(names)}")    # see how many items exist
print(f"Valid indices: 0 to {len(names) - 1}")  # shows the safe range

# -------------------------
# 5️⃣ Quick Reference — Index Errors Cheat Sheet
# -------------------------
# | Mistake                        | Error                        |
# |--------------------------------|------------------------------|
# | names[5] on a 5-item list      | ❌ IndexError (max is 4)     |
# | names[-1] on a non-empty list  | ✅ Safe — returns last item  |
# | names[-1] on an empty list     | ❌ IndexError (nothing there)|
# | print(names) when confused     | ✅ Always helps debug!       |

print("\n✅ All index error exercises completed successfully!")
