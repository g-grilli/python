print("I am thinking of a number between 1 and 10")
import random
nums = random.randint(1,10)
guess = input("What's the number? ")
while guess != nums:
  if guess != nums:
      print("Nope, try again")
      guess = input("What's the number? ")
      break
print("Yes! You win!")


# You will implement a guess-the-number game where the player has to try
# guessing a secret number until he gets it right. For now, you will "hard code"
# the secret number to 5 (just set it to five like secret_number = 5). You will
# prompt the player to enter a number again and again, each time comparing his
# input to the secret number. To to that, you will need to write a while loop.
# If he guesses correctly, you will print "You win!", otherwise, you will prompt
# for a number again.

# Example session:

# $ python guess_the_number.py
# I am thinking of a number between 1 and 10.
# What's the number? 3
# Nope, try again.
# What's the number? 9
# Nope, try again.
# What's the number? 5
# Yes! You win!
