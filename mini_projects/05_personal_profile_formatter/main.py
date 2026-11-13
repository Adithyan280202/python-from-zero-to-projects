
# Mini Project 05
# Personal Profile Formatter

print("=" * 45)
print("         PERSONAL PROFILE FORMATTER")
print("=" * 45)

# Collect user information
full_name = input("Enter your full name: ")
email = input("Enter your email address: ")
place = input("Enter your place: ")
profession = input("Enter your profession: ")

# Format the information
clean_name = full_name.strip()
clean_email = email.strip()
clean_place = place.strip()
clean_profession = profession.strip()

formatted_name = clean_name.title()
username = clean_name.lower().replace(" ", ".")
formatted_email = clean_email.lower()
formatted_place = clean_place.title()
formatted_profession = clean_profession.title()

# Calculate string lengths
name_length = len(clean_name)
email_length = len(formatted_email)

# Display data types
print("\n" + "=" * 45)
print("              DATA TYPES")
print("=" * 45)

print("Name:", type(clean_name))
print("Email:", type(clean_email))
print("Place:", type(clean_place))
print("Profession:", type(clean_profession))
print("Username:", type(username))
print("Name Length:", type(name_length))

# Display formatted profile
print("\n" + "=" * 45)
print("            PERSONAL PROFILE")
print("=" * 45)

print(f"Full Name    : {formatted_name}")
print(f"Username     : {username}")
print(f"Email        : {formatted_email}")
print(f"Place        : {formatted_place}")
print(f"Profession   : {formatted_profession}")

print("-" * 45)
print(f"Name Length  : {name_length} characters")
print(f"Email Length : {email_length} characters")

print("=" * 45)
print("       PROFILE GENERATED SUCCESSFULLY!")
print("=" * 45)
