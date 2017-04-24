print("I am thinking of a number between 1 and 10")
import random
nums = random.randint(1,10)
print(nums)
tries = 5
guess = int(input("What's the number? "))
if guess == nums:
    print("Yes! You win!")
play = "Y"
while guess !=  nums and play == "Y":
  if guess > nums and tries > 1:
      tries = tries - 1
      print("{} is too high".format(guess))
      print("You have {} guesses left.".format(tries))
      guess = int(input("What's the number? "))
  elif guess < nums and tries > 1:
      tries = tries - 1
      print("{} is too low".format(guess))
      print("You have {} guesses left.".format(tries))
      guess = int(input("What's the number? "))
  elif tries <= 1:
      print("You ran out of guesses")
      break
if guess == nums and tries != 5:
    print("Yes! You win!")
print("Goodbye")    
