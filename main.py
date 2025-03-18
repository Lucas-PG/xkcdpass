import random
import string

with open("words.txt", "r") as file:
    words = [word.strip() for word in file.readlines()]

min_length = 5
filtered_words = [word for word in words if len(word) >= min_length]

if len(filtered_words) < 5:
    print(f"Error: Not enough words of length {min_length} or greater.")
else:
    random_words = random.sample(filtered_words, 5)

    capitalized_words = [word.capitalize() for word in random_words]

    base_password = "".join(capitalized_words)

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    random_special = random.choice(special_chars)
    random_number = random.randint(0, 9)

    password = f"{'-'.join(capitalized_words)}{random_special}{random_number}"

    print(password)
