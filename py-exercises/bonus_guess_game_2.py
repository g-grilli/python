play = input("would you like to play a guessing game?(yes or no) ")
correct = "no"
nums = 50
count = 0
max = 100
min = 0
while play == "yes":
    if count == 0:
        print("Please select an number between 0 and 100")
        count += 1
    if count > 0 and correct == "no":
        correct = input("Is the number {} ? ".format (nums))
        if correct == "no":
            status = input("Is your number 'higher' or 'lower'? ")
            count += 1
            if status == "higher":
                nums = int((nums + max) /2)
            if status == "lower":
                nums = int((nums + min) /2)
        if correct == "yes":
            print("It took {} tries to guess your number".format (count))


print("Have a nice life!")
