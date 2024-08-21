import random

user_range = int(input("Enter a number higher than 0 for the range: "))


def guess_number(x):
    low = 1
    high = x
    user_feedback = ''

    while user_feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        user_feedback = input(f"Is {guess} too high (H) or too low (L), or Correct (C)? ".lower())
        if user_feedback == 'h':
            high = guess - 1
        elif user_feedback == 'l':
            low = guess + 1

    print(f"Yay, the computer was able to guess your number, {guess}")


guess_number(user_range)
