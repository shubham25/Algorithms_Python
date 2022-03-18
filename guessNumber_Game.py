#! /usr/bin/env python3
from random import randint
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect Run")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    right_ans = randint(a, b)
    # print(right_ans)
    prompt = "\nTake your  First guess ! :  "
    closeness = -1
    while (user_guess := input(prompt)).isdigit():
        user_guess = int(user_guess)
        if user_guess > b or user_guess < a:
            print(f"\n Out of Range Guess Fool, Range is {a} to {b} !!  ")
            continue

        if user_guess == right_ans:
            print(" You got it Right King !!")
            break
        else:
            if closeness == -1:
                closeness = abs(right_ans - user_guess)
                prompt = "\nGuess Again:  "
            else:
                new_close = abs(right_ans - user_guess)
                print("Warmer") if new_close < closeness else print("Colder")
                closeness = new_close

    print("\n Thanks for playing. Goodbye! ")