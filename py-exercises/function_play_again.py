#!usr/bin/env python 3
def play_again():
    pAgain = input("Do you wnat to play again?(Y or N) ")
    if pAgain == 'Y':
        return True
    elif pAgain == 'N':
        return False
    else:
        print("try again")

if __name__ == "__main__":
    play_again()

# Write a function that prompts the user for input, asking them "Do you want to
# play again (Y on N)?". If the user answers "Y", the function should return True,
# otherwise, it should return False.
