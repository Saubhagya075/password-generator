# Password Generator with Strength Checker

A simple Python CLI tool that generates a random, customizable password and checks how strong it is.

By Saubhagya Gupta — BCA student, Invertis University, Bareilly.

## Features

- Choose password length (4–32)
- Choose character types: small letters, capital letters, numbers, symbols
- Uses `random` module for random passwords
- Strength checker based on length and character variety
  - Weak / Medium / Strong / Very Strong

## How to run

```bash
python password_generator.py
```

Then answer the questions:
1. Password length
2. Include small letters? (y/n)
3. Include capital letters? (y/n)
4. Include numbers? (y/n)
5. Include symbols? (y/n)

Example:

```
=== Password Generator with Strength Checker ===

Password length (8-32): 12
Include small letters (a-z)? (y/n): y
Include capital letters (A-Z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include symbols (!@#$)? (y/n): y

Your password is:
s'}(Z*jb7EC<
Strength: Strong (4/5)
```

## Files

- `password_generator.py` — main program

## Skills used

Python, functions, `random`, `string`, CLI input/output
