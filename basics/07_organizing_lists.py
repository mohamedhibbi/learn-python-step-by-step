# ======================================================
# Organizing Lists in Python
# Author: Mohamed hibbi
# Description: Examples of sorting, reversing, and
# finding the length of lists using sort(), sorted(),
# reverse(), and len().
# ======================================================

# -------------------------
# 1️⃣ sort() — Permanent Alphabetical Sort
# -------------------------
# sort() is a METHOD called directly on the list
# It changes the list permanently — original order is lost!

cars = ["mercedes", "bmw", "bugatti", "audi", "firari"]
cars.sort()  # permanently sorts A → Z
print("Sorted A → Z:", cars)

# You can also sort in reverse alphabetical order permanently
cars = ["mercedes", "bmw", "bugatti", "audi", "firari"]
cars.sort(reverse=True)  # permanently sorts Z → A
print("Sorted Z → A:", cars)

# -------------------------
# 2️⃣ sorted() — Temporary Sort (Original Unchanged)
# -------------------------
# sorted() is a FUNCTION — not a method
# It returns a sorted copy but leaves the original list intact

cars = ["mercedes", "bmw", "bugatti", "audi", "firari"]
print(f"\nHere is the original list: {cars}")
print(f"Here is the sorted list: {sorted(cars)}")        # A → Z temporarily
print(f"Here is the original list again: {cars}")        # still original!
print(f"Here is sorted in reverse: {sorted(cars, reverse=True)}")  # Z → A temporarily
print(f"Here is the original list again: {cars}")        # still original!

# Key difference:
# sort()   → METHOD  → changes list permanently
# sorted() → FUNCTION → keeps original, returns new sorted list

# -------------------------
# 3️⃣ reverse() — Reverse the Order Permanently
# -------------------------
# reverse() is a METHOD that flips the list order permanently
# Calling it twice brings you back to the original order!

cars = ["mercedes", "bmw", "bugatti", "audi", "firari"]
cars.reverse()
print(f"\nThis is the list reversed: {cars}")
cars.reverse()  # calling reverse() again undoes it!
print(f"Back to original list: {cars}")

# -------------------------
# 4️⃣ len() — Find the Length of a List
# -------------------------
# len() is a FUNCTION that returns the number of items in a list

cars = ["mercedes", "bmw", "bugatti", "audi", "firari"]
print(f"\nNumber of cars in the list: {len(cars)}")

# -------------------------
# 5️⃣ Try It Yourself — Places to Visit
# -------------------------
# Applying all four concepts to a personal list of places

places = ["makkah", "al madinah", "japan", "australia", "palestine"]

print(f"\nThis is the original order: {places}")

# sorted() — temporary sort
print(f"This is the list in temporarily sorted order: {sorted(places)}")
print(f"It's still in the original order: {places}")

# sorted(reverse=True) — temporary reverse sort
print(f"This is the list sorted in reverse alphabetical order: {sorted(places, reverse=True)}")
print(f"It's still in the original order: {places}")

# reverse() — permanent reverse
places.reverse()
print(f"The list is now reversed: {places}")
places.reverse()
print(f"Back to original: {places}")

# sort() — permanent alphabetical sort
places.sort()
print(f"This is the list sorted in alphabetical order (permanent): {places}")

# sort(reverse=True) — permanent reverse alphabetical sort
places.sort(reverse=True)
print(f"This is the list sorted in reversed alphabetical order (permanent): {places}")

# len() — count the items
print(f"This is the number of places I want to visit: {len(places)}")

# -------------------------
# 6️⃣ Summary — Quick Reference
# -------------------------
# | Method/Function   | Type     | Permanent? | Description                     |
# |-------------------|----------|------------|---------------------------------|
# | sort()            | Method   | ✅ Yes     | Sorts list A→Z permanently      |
# | sort(reverse=True)| Method   | ✅ Yes     | Sorts list Z→A permanently      |
# | sorted()          | Function | ❌ No      | Returns sorted copy, A→Z        |
# | sorted(rev=True)  | Function | ❌ No      | Returns sorted copy, Z→A        |
# | reverse()         | Method   | ✅ Yes     | Reverses list order permanently |
# | len()             | Function | ❌ No      | Returns number of items         |

print("\n✅ All organizing list exercises completed successfully!")
