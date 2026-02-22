# ======================================================
# Nesting
# Author: Mohamed Hibbi
# Description: Storing lists inside dictionaries,
# dictionaries inside lists, and dictionaries
# inside other dictionaries.
# ======================================================

# -------------------------
# 3️⃣2️⃣ A List of Dictionaries
# -------------------------
# When you need to store multiple dictionaries of the same type,
# put them all inside a list. Each dictionary represents one item.

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 5}
alien_2 = {"color": "blue", "points": 5}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# -------------------------
# 3️⃣3️⃣ Generating a Fleet With range()
# -------------------------
# Instead of creating each dictionary manually,
# use range() and append() to generate many dictionaries at once.

aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "speed": "slow", "points": 5}
    aliens.append(new_alien)

# Print only the first 5 to keep output clean
for alien in aliens[:5]:
    print(alien)
print("....")
print(f"Total number of aliens created is {len(aliens)}")

# -------------------------
# 3️⃣4️⃣ Modifying Items in a List of Dictionaries
# -------------------------
# You can loop through a slice of the list and modify
# each dictionary's values directly — changes are permanent.

aliens = []
for number in range(30):
    new_alien = {"color": "green", "speed": "slow", "points": 5}
    aliens.append(new_alien)

# Change the first 3 aliens from green to yellow
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:3]:
    print(alien)

# -------------------------
# 3️⃣5️⃣ A List Inside a Dictionary
# -------------------------
# Use a list as a value when a key can have multiple values.
# Here a pizza can have many toppings stored in a list.

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "black pepper", "extra cheese"],
}
print(f"\nYou ordered a {pizza['crust']} pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

# -------------------------
# 3️⃣6️⃣ Multiple Values Per Person
# -------------------------
# Each person can have a list of favorite languages as their value.
# Loop through the dictionary, then loop through each person's list.

favorite_languages = {
    "mohamed": ["python", "javascript"],
    "sara": ["c", "python"],
    "hanae": ["ruby", "php"],
    "mimi": ["go", "javascript"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()} Favorite Languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Use extend() + set() to collect and deduplicate all languages
# extend() unwraps the list and adds each item individually
# set() removes duplicates
all_languages = []
for language in favorite_languages.values():
    all_languages.extend(language)

print(f"\nThe languages that have been mentioned are:")
for language in set(all_languages):
    print(f"\t{language.title()}")

# -------------------------
# 3️⃣7️⃣ A Dictionary Inside a Dictionary
# -------------------------
# Use nested dictionaries when each key maps to structured information.
# Here each username maps to a full profile dictionary.

users = {
    "mohamed": {
        "first_name": "mohamed",
        "last_name": "hibbi",
        "email": "medhibbi7@gmail.com",
        "country": "morocco",
    },
    "sara": {
        "first_name": "sara",
        "last_name": "hibbi",
        "email": "sarahibbi@gmail.com",
        "country": "morocco",
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info["country"]
    email = user_info["email"]
    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")
    print(f"Email: {email}")

# -------------------------
# 3️⃣8️⃣ Try It Yourself - Pets
# -------------------------
# Store pet information in a dictionary of dictionaries.
# Each pet's name is the key, and their details are the value.

pets = {
    "max": {
        "animal": "dog",
        "owner": "mohamed",
        "favorite_food": "chicken",
    },
    "mimi": {
        "animal": "cat",
        "owner": "sara",
        "favorite_food": "beef",
    },
}
for name, pet_info in pets.items():
    print(f"\n{name.title()} is a {pet_info['animal'].title()}")
    print(f"\tThe owner is: {pet_info['owner'].title()}")
    print(f"\tFavorite food: {pet_info['favorite_food'].title()}")

# -------------------------
# 3️⃣9️⃣ Summary - Quick Reference
# -------------------------
# | Nesting Type              | Structure                                 |
# |---------------------------|-------------------------------------------|
# | List of dictionaries      | aliens = [alien_0, alien_1, alien_2]      |
# | Generate with range()     | for i in range(30): list.append({...})    |
# | List inside dictionary    | {"toppings": ["mushrooms", "cheese"]}     |
# | Dictionary inside dict    | {"user": {"first": "mohamed"}}            |
# | extend() vs append()      | extend() unwraps list, append() nests it  |
# | Deduplicate values        | set(all_items)                            |

print("\n✅ All nesting exercises completed successfully!")
