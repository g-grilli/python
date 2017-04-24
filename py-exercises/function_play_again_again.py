#!usr/bin/env python 3
def play_again():
    status = False
    while status == False:
        pAgain = input("Do you want to play again?('Y' or 'N') ")
        if pAgain == 'Y' or pAgain == 'N':
            status = True
            if pAgain == 'Y':
                return True
            else:
                return False
        else:
            print('that is incorrect.')
            status = False

if __name__ == "__main__":
    play_again()


#Write a function that asks the user whether they want to play again last the
#previous problem. Except this time, they have to answer with either "Y" or "N",
#if they give an invalid input, it should say "Invalid input." and prompt the
#user again for an answer. When the user finally gives a valid input, the
#function will return True if it was "Y", and False if it was "N".
