# ======================================================
# Dictionaries
# Author: Mohamed Hibbi
# Description: Creating and accessing dictionaries,
# adding, modifying, and removing key-value pairs,
# looping through dictionaries, and nesting.
# ======================================================

# -------------------------
# 1️⃣4️⃣ What is a Dictionary?
# -------------------------
# A dictionary stores key-value pairs wrapped in curly braces {}
# Each key is connected to a value using a colon :
# Keys and values can be strings, numbers, or even lists

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])   # Access value using its key
print(alien_0["points"])

# -------------------------
# 1️⃣5️⃣ Adding Key-Value Pairs
# -------------------------
# Dictionaries are dynamic — you can add new key-value pairs at any time
# Just use dict[new_key] = new_value

alien_0 = {"color": "green", "points": 5}
print(f"Original dictionary: {alien_0}")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(f"After adding positions: {alien_0}")

# -------------------------
# 1️⃣6️⃣ Modifying Values
# -------------------------
# To change a value, refer to its key and assign a new value

alien_0 = {"color": "green", "points": 5}
print(f"The alien color is {alien_0['color']}")

alien_0["color"] = "yellow"
print(f"The alien color is now {alien_0['color']}")

# -------------------------
# 1️⃣7️⃣ Starting With an Empty Dictionary
# -------------------------
# Sometimes it's cleaner to start empty and fill it in with a loop or logic

alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(f"Empty dictionary now filled: {alien_0}")

# -------------------------
# 1️⃣8️⃣ A Practical Example - Tracking an Alien
# -------------------------
# Dictionaries are great for storing related information about one thing

alien_0 = {
    "x_position": 0,
    "y_position": 25,
    "color": "green",
    "speed": "medium",
}
print(f"Original position: {alien_0['x_position']}")

# Move the alien based on its speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")

# -------------------------
# 1️⃣9️⃣ Removing Key-Value Pairs With del
# -------------------------
# Use del to permanently remove a key-value pair from a dictionary

alien_0 = {
    "x_position": 0,
    "y_position": 2,
    "color": "red",
    "speed": "medium",
    "points": 5,
}
print(f"The original dictionary is {alien_0}")

del alien_0["points"]
print(f"Now the new dictionary is {alien_0}")

# -------------------------
# 2️⃣0️⃣ A Dictionary of Similar Objects
# -------------------------
# Dictionaries are perfect for storing the same type of info about many things
# Here each person's name is a key, and their favorite language is the value

favorite_languages = {
    "mohamed": "python",
    "sarah": "c",
    "hanae": "javascript",
    "mimi": "java",
}
for name in favorite_languages.keys():
    print(f"{name} favorite language is {favorite_languages[name]}")

# -------------------------
# 2️⃣1️⃣ Using get() to Access Values Safely
# -------------------------
# Accessing a key that doesn't exist causes a KeyError
# get() lets you provide a default value instead of crashing
# Syntax: dictionary.get(key, default_value)

alien_0 = {"color": "green", "speed": "slow"}

# 'points' key doesn't exist — get() returns the default message
point_value = alien_0.get("points", "No point value assigned.")
print(f"Point value: {point_value}")

# 'color' key exists — get() returns its value normally
color_value = alien_0.get("color", "No color assigned.")
print(f"Color value: {color_value}")

# -------------------------
# 2️⃣2️⃣ Looping Through All Key-Value Pairs With .items()
# -------------------------
# .items() returns each key-value pair so you can unpack both at once

user_0 = {
    "username": "mohamedhibbi",
    "first": "mohamed",
    "last": "hibbi",
}
for key, value in user_0.items():
    print(f"the key is: {key}")
    print(f"the value is: {value}")

# Another example with title() formatting
favorite_languages = {
    "mohamed": "python",
    "sara": "c",
    "hanae": "javascript",
    "mimi": "java",
}
for name, language in favorite_languages.items():
    print(f"{name.title()} Favorite language is {language.title()}\n")

# -------------------------
# 2️⃣3️⃣ Looping Through Keys With .keys()
# -------------------------
# Use .keys() when you only need the keys
# You can also check if a key belongs to a specific group

favorite_languages = {
    "mohamed": "python",
    "sara": "c",
    "hanae": "javascript",
    "mimi": "java",
    "sisat": "ruby",
}

# Loop through all keys
for key in favorite_languages.keys():
    print(f"the key is {key.title()}")

# Check if a key belongs to a group and print a special message
family_members = ["mohamed", "sara", "hanae"]
for name in favorite_languages.keys():
    print(f"the name is {name.title()}")
    if name in family_members:
        print(f"Hi {name.title()}! I see your favorite language is: {favorite_languages[name]}\n")

# -------------------------
# 2️⃣4️⃣ Looping Through Keys in Order With sorted()
# -------------------------
# Dictionaries preserve insertion order in Python 3.7+
# Use sorted() to loop through keys alphabetically

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} Thank you For taking the poll")

# -------------------------
# 2️⃣5️⃣ Looping Through Values With .values()
# -------------------------
# Use .values() when you only care about the values, not the keys

print("Languages that have been mentioned is: ")
for value in favorite_languages.values():
    print(f"\t{value.upper()}")

# -------------------------
# 2️⃣6️⃣ Removing Duplicates From Values With set()
# -------------------------
# .values() can return duplicates if multiple people chose the same thing
# Wrap it in set() to get only unique values

favorite_languages = {
    "mohamed": "python",
    "sara": "c",
    "hanae": "javascript",
    "mimi": "java",
    "sisat": "ruby",
    "zaid": "python",   # duplicate!
}
print("Languages that have been mentioned is: ")
for value in set(favorite_languages.values()):
    print(f"\t{value.upper()}")

# -------------------------
# 2️⃣7️⃣ Try It Yourself - Glossary, Rivers & Pets
# -------------------------

# Exercise 6-4: Glossary 2 - Loop through and print keys neatly
words = {
    "if statement": "execute code consider on False or True",
    "for loop": "take each name inside list or dictionary or whatever you want and add it to a variable then loop",
    "dictionary": "take a key and a value",
    "lists": "inside []",
    "tuples": "inside ()",
    "set": "make sure no repetitive included within a list",
}
print(f"the key values used in this dictionary is:")
for key in words.keys():
    print(key.upper())

# Exercise 6-5: Rivers - Loop through three ways
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "seine": "france",
    "mississippi": "united states",
    "yangtze": "china",
}
for key, value in rivers.items():
    print(f"the river {key.title()} runs through {value.title()}")

print(f"\nthe names of each river included in the dictionary are:")
for name in rivers.keys():
    print(name.title())

print("\nThe Name of each country included in the dictionary are:")
for country in set(rivers.values()):
    print(country.title())

# Exercise 6-8: Pets - Loop through and print each pet's info
pets = {
    "rex": "dog",
    "luna": "cat",
    "kiwi": "parrot",
}
for name, type in pets.items():
    print(f"\n{name.title()} is a {type}")

# -------------------------
# 2️⃣8️⃣ Nesting - A List of Dictionaries
# -------------------------
# Store multiple dictionaries inside a list
# Each dictionary represents one item (e.g. one alien)

alien_0 = {"color": "green", "points": 5, "speed": "slow"}
alien_1 = {"color": "yellow", "points": 10, "speed": "medium"}
alien_2 = {"color": "red", "points": 15, "speed": "fast"}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# -------------------------
# 2️⃣9️⃣ Nesting - A List Inside a Dictionary
# -------------------------
# Use a list as a value when a key can have multiple values

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
print(f"\nYou ordered a {pizza['crust']}-crust pizza with these toppings:")
for topping in pizza["toppings"]:
    print(f"\t- {topping}")

# Another example — each person has multiple favorite languages
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages:")
    for language in languages:
        print(f"\t{language.title()}")

# -------------------------
# 3️⃣0️⃣ Nesting - A Dictionary Inside a Dictionary
# -------------------------
# Use nested dictionaries to store structured info per key
# Each key maps to a whole dictionary of details

users = {
    "mohamedhibbi": {
        "first": "mohamed",
        "last": "hibbi",
        "location": "morocco",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation:  {location.title()}")

# -------------------------
# 3️⃣1️⃣ Summary - Quick Reference
# -------------------------
# | Concept                  | Syntax / Example                        |
# |--------------------------|------------------------------------------|
# | Create dictionary        | d = {"key": "value"}                    |
# | Access value             | d["key"]                                 |
# | Add / Modify value       | d["key"] = "new_value"                  |
# | Remove key-value pair    | del d["key"]                             |
# | Safe access              | d.get("key", "default")                 |
# | Loop key-value pairs     | for k, v in d.items()                   |
# | Loop keys only           | for k in d.keys()                       |
# | Loop keys in order       | for k in sorted(d.keys())               |
# | Loop values only         | for v in d.values()                     |
# | Unique values            | for v in set(d.values())                |
# | List of dictionaries     | aliens = [alien_0, alien_1, alien_2]    |
# | List inside dictionary   | {"toppings": ["mushrooms", "cheese"]}   |
# | Dictionary inside dict   | {"user": {"first": "mohamed"}}          |

print("\n✅ All dictionary exercises completed successfully!")
