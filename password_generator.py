# Password Generator with Strength Checker
# Made by Saubhagya Gupta

import random
import string


def generate_password(length, upper, lower, digit, symbol):
    chars = ""
    if upper == "y":
        chars = chars + string.ascii_uppercase
    if lower == "y":
        chars = chars + string.ascii_lowercase
    if digit == "y":
        chars = chars + string.digits
    if symbol == "y":
        chars = chars + string.punctuation

    if chars == "":
        return "Please select at least one option"

    password = ""
    i = 0
    while i < length:
        password = password + random.choice(chars)
        i = i + 1
    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score = score + 1
    if len(password) >= 12:
        score = score + 1

    has_small = False
    has_capital = False
    has_number = False
    has_symbol = False

    for ch in password:
        if ch.islower():
            has_small = True
        if ch.isupper():
            has_capital = True
        if ch.isdigit():
            has_number = True
        if ch in string.punctuation:
            has_symbol = True

    types = 0
    if has_small:
        types = types + 1
    if has_capital:
        types = types + 1
    if has_number:
        types = types + 1
    if has_symbol:
        types = types + 1

    if types >= 3:
        score = score + 1
    if types == 4:
        score = score + 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


print("Password Generator with Strength Checker")
print()

length = int(input("Enter password length: "))

lower = input("Include small letters? (y/n): ")
upper = input("Include capital letters? (y/n): ")
digit = input("Include numbers? (y/n): ")
symbol = input("Include symbols? (y/n): ")

password = generate_password(length, upper, lower, digit, symbol)

print()
print("Your password is:", password)
print("Strength:", check_strength(password))
