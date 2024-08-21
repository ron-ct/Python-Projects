import random

range_num = int(input("Enter a number of your choice for the range: "))


def guess_func(x):
    guess = random.randint(1, x)
    user_answer = 0

    while user_answer != guess:
        user_answer = int(input("Guess a number: "))
        if user_answer > guess:
            print("Sorry, Too high")
        elif user_answer < guess:
            print("Sorry, Too low")

    print("Yay, you passed")


guess_func(range_num)
