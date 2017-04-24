name = input("What is your name?")
name = name.upper()
print("HELLO, {}!".format (name))
nums = len(name)
print("YOUR NAME HAS {} LETTERS IN IT! AWESOME!".format (nums))

Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name. Example session:

# $ python hello2.py
# WHAT IS YOUR NAME? Toby
# HELLO, TOBY!
# YOUR NAME HAS 4 LETTERS IN IT! AWESOME!
