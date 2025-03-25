
import string
import re

def check_password_length(password):
    length = len(password)
    score = 0
    suggestions = []

    if length > 8:
        score += 1
    else:
        suggestions.append("Increase the password length to at least 8 characters.")
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1
    return score, suggestions

def check_character_types(password):
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_special = any(c in string.punctuation for c in password)
    has_digit = any(c.isdigit() for c in password)
    character_types = [has_uppercase, has_lowercase, has_special, has_digit]
    score = 0
    suggestions = []
    if has_uppercase:
        score += 1
    else:
        suggestions.append("Try including capital letters to increase password complexity")
    if has_lowercase:
        score += 1
    else:
        suggestions.append("Try using lower case letters to increase password complexity")
    if has_special:
        score += 1
    else:
        suggestions.append("Try including special characters to increase password complexity")
    if has_digit:
        score += 1
    else:
        suggestions.append("Try including digits to increase password complexity")
    return score, suggestions

def assess_password_strength(score):
    if score < 2:
        print(f"This password is very weak. Total score: {score}. It is highly vulnerable to cracking.")
    elif score < 4:
        print(f"This password is quite weak. Total score: {score} It could be cracked relatively easily.")
    elif score == 4:
        print(f"This password is ok. Total score: {score} It has some basic security, but could be improved.")
    elif score > 4 and score < 6:
        print(f"This password is good. Total score: {score} It offers a reasonable level of security.")
    else:
        print(f"This password is strong. Total score: {score} It is likely to be resistant to most cracking attempts.")


password = input("Please enter in the password you wish to analyse here: ")

with open('Common_Passwords.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("This password is a commonly used password and is easily guessable.")
    exit()
else:
    print("Password is not recognised as a commonly used password")

length_score, length_suggestions = check_password_length(password)
character_score, character_suggestions = check_character_types(password)
total_score = length_score + character_score

all_suggestions = length_suggestions + character_suggestions

print(f"Password length score: {length_score}")
print(f"Character type score: {character_score}")

assess_password_strength(total_score)

if all_suggestions:
    print("\nSuggestions for improvement: ")
    for suggestions in all_suggestions:
        print(f"- {suggestions}")