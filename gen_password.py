import random

# Ask for a valid length (with letter control)
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length > 0:
            break
        else:
            print("ERROR: Invalid number")
    except ValueError:
        print("ERROR: You must enter a number, not a letter")

# Character groups
groups = [
    ("uppercase letters", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("lowercase letters", "abcdefghijklmnopqrstuvwxyz"),
    ("numbers", "0123456789"),
    ("symbols", "!@#$%&/?¿¡*+._:;=<>-")
]

full_string = ""
mandatory = []

# Ask the user which groups to include
for name, characters in groups:
    answer = input(f"Do you want to include {name}? (y/n) ").lower()
    if answer == "y":
        full_string += characters
        mandatory.append(random.choice(characters))

# Validate that at least one type is selected
while full_string == "":
    print("ERROR: You must include at least one character type")
    for name, characters in groups:
        answer = input(f"Do you want to include {name}? (y/n) ").lower()
        if answer == "y":
            full_string += characters
            mandatory.append(random.choice(characters))

# Generate the remaining characters
remaining = length - len(mandatory)
rest = [random.choice(full_string) for _ in range(remaining)]

# Combine and shuffle
password_list = mandatory + rest
random.shuffle(password_list)

# Convert to string
password = "".join(password_list)

print("Generated password:", password)