# A simple Password generator that uses user feedback to create a random password of specified length
import random
import string

def generatePassword(min_length, number= True, special = True):

    letters = string.ascii_letters
    numbers = string.digits
    specials = string.punctuation

    characters = letters

    if number:
        characters += numbers


    if special:
        characters += specials

    pwd = ""
    hasNumbers = False
    hasSpecial = False
    meetsCriteria = False

    while not meetsCriteria or len(pwd) < min_length:
        new_character = random.choice(characters)
        pwd += new_character

        if new_character in numbers:
            hasNumbers = True
        elif new_character in specials:
            hasSpecial = True
        
        meetsCriteria = True
        if number:
            meetsCriteria = hasNumbers
        elif special:
            meetsCriteria = meetsCriteria and hasSpecial
    
    return pwd

min_length = int(input("Enter the required length of your password: "))
number = input("Do you want numbers in the password? (y/n)").lower() == "y"
special = input("Do you want Special Characters in your password? (y/n)").lower() == "y"

password = generatePassword(min_length, number, special)
print(password)