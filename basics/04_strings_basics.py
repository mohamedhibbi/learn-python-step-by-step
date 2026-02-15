"""
Basic Python – Strings & Formatting
This file demonstrates:
1. Variables
2. f-strings
3. String methods
4. Escape characters
5. Whitespace stripping
"""

# ----------------------------
# 1️⃣ Variables and f-strings
# ----------------------------

name = "Mohamed Hibbi"
print(f"Hello {name}, would you like to learn some Python today?")


# ----------------------------
# 2️⃣ String case methods
# ----------------------------

print("\n--- String Case Methods ---")
print(name.lower())   # convert to lowercase
print(name.upper())   # convert to uppercase
print(name.title())   # capitalize each word


# ----------------------------
# 3️⃣ Escape characters
# ----------------------------

print("\n--- Escape Characters ---")
print('\tAlbert Einstein once said,')
print('\t"A person who never made a')
print('\tmistake never tried anything new."')


# ----------------------------
# 4️⃣ Using variables properly
# ----------------------------

famous_person = "Albert Einstein"

message = (
    f'\t{famous_person} once said,\n'
    f'\t"A person who never made a\n'
    f'\tmistake never tried anything new."'
)

print("\n--- Using Variables ---")
print(message)


# ----------------------------
# 5️⃣ Removing whitespace
# ----------------------------

pet_name = "    sisat    "

print("\n--- Whitespace Cleaning ---")
print(f"Original: '{pet_name}'")
print(f"lstrip(): '{pet_name.lstrip()}'")
print(f"rstrip(): '{pet_name.rstrip()}'")
print(f"strip():  '{pet_name.strip()}'")

