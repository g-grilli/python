amount = float(input("Total bill amount? "))
service_level = input("Level of service?(good, fair, bad) ")
split = int(input("Split how many ways? "))
if service_level == "good":
    tip_amount = amount * .20
    total_bill = amount + tip_amount
    split_amount = total_bill / split
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
    print("total bill: ${:.2f}".format (split_amount))
elif service_level == "fair":
    tip_amount = amount * .15
    total_bill = amount + tip_amount
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
    print("total bill: ${:.2f}".format (split_amount))
elif service_level == "bad":
    tip_amount = amount * .10
    total_bill = amount + tip_amount
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
    print("total bill: ${:.2f}".format (split_amount))
else:
    print("I am not sure I understand")

# Prompt the user for two things:

# The total bill amount:
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount).
# The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%
# Example session:

# $ python tip_calc.py
# Total bill amount? 100
# Level of service? good
# Tip amount: $20.00
# Total amount: $120.00
# $ python tip_calc.py
# Total bill amount? 48
# Level of service? bad
# Tip amount: $4.80
# Total amount: $52.80
# Hints:

# To format a float number as a dollar value, use Python's formatting syntax:
# "{:.2f}".format(amount)

# Allow the ability to divide the check into a equal parts amount a number of
# people. The user will enter the number of people to be divided amongst.
# Example session:

# $ python tip_calc2.py
# Total bill amount? 100
# Level of service? good
# Split how many ways? 5
# Tip amount: $20.00
# Total amount: $120.00
# Amount per person: $24.00
