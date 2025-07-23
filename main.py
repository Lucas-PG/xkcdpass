#!/usr/bin/env python3
import argparse
import os
import random
import string

script_dir = os.path.dirname(os.path.realpath(__file__))
words_path = os.path.join(script_dir, "words.txt")

with open(words_path, "r") as file:
    words = [line.strip() for line in file.readlines()]

min_length = 5
all_words = [word for word in words if len(word) >= min_length]

MAN_TEXT = """
XKCD Password Method Explanation:
Inspired by XKCD comic #936 (https://xkcd.com/936/), this method creates strong, memorable passwords
using random common words instead of complex strings of characters. The idea is that a passphrase
like "Jungle-Tornado-Silver-Galaxy-Puzzle" is easier to remember than "Tr0ub4dor&3xtr1c4t3", yet
still secure due to its length and randomness.

Why It Works:
- Humans struggle with random character strings but excel at remembering phrases or stories.
- Length matters more than complexity for resisting brute-force attacks.
- Random word selection ensures high entropy (unpredictability).

Password Complexity in This Script:
- Wordlist: Custom list (assuming 7,776 words, adjust based on your file), filtered to 5+ letters.
- Scheme: 5 random words, first letter capitalized, joined with '-', plus 1 special char (26 options)
  and 1 digit (10 options).
- Total combinations: 7,776^5 * 26 * 10 = 7.389 * 10^21 (7.389 sextillion).
- Cracking time (offline, 100 billion guesses/sec): ~7.389 × 10¹⁰ seconds = ~2,342 years.
- Strength: Extremely strong for online attacks (rate-limited) and robust against offline cracking
  with modern hashing (e.g., bcrypt). Main risks are reuse or phishing, not brute force.
"""


def generate_password(filtered_words_by_letter, letters):
    """Generate a password with one word per specified letter."""
    if len(letters) < 5:
        return f"Error: Need at least 5 letters to generate a 5-word password (got {len(letters)})."

    for letter in letters[:5]:  # Take first 5 letters if more are provided
        if not any(word.startswith(letter) for word in filtered_words_by_letter):
            return f"Error: No words of length {min_length}+ start with '{letter}'."

    random_words = []
    for letter in letters[:5]:
        matching_words = [
            word for word in filtered_words_by_letter if word.startswith(letter)
        ]
        random_words.append(random.choice(matching_words))

    capitalized_words = [word.capitalize() for word in random_words]
    base_password = "-".join(capitalized_words)
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    random_special = random.choice(special_chars)
    random_number = random.randint(0, 9)
    return f"{base_password}{random_special}{random_number}"


def main():
    parser = argparse.ArgumentParser(
        description="Generate an XKCD-style password.",
        add_help=False,
    )
    parser.add_argument(
        "-l",
        "--letters",
        type=str,
        help="Comma-separated letters to filter words by (e.g., 'l,u,c,a,s'). One word per letter.",
    )
    parser.add_argument(
        "-m",
        "--man",
        action="store_true",
        help="Display explanation of the XKCD method and password complexity.",
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="Show this help message."
    )

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return

    if args.man:
        print(MAN_TEXT)
        return

    if args.letters:
        letters = [letter.lower() for letter in args.letters.split(",")]
        password = generate_password(all_words, letters)
    else:
        password = generate_password(
            all_words, random.sample([word[0] for word in all_words], 5)
        )

    print(password)


if __name__ == "__main__":
    main()
