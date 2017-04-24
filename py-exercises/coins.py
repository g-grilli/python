coins = 0
print("You have {} coins.".format (coins))
answer = input("Do you want another? ")
while answer != "no":
  if answer != "no":
      coins = coins + 1
      print("You have {} coins.".format (coins))
      answer = input("Do you want another? ")
  else:
      print("You have {} coins.".format (coins))
print("bye")

# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

# $ python coins.py
# You have 0 coins.
# Do you want another? yes
# You have 1 coins.
# Do you want another? yes
# You have 2 coins.
# Do you want another? no
# Bye
