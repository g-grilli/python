amount = float(input("Total bill amount? "))
service_level = input("Level of service?(good, fair, bad) ")
if service_level == "good":
    tip_amount = amount * .20
    total_bill = amount + tip_amount
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
elif service_level == "fair":
    tip_amount = amount * .15
    total_bill = amount + tip_amount
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
elif service_level == "bad":
    tip_amount = amount * .10
    total_bill = amount + tip_amount
    print("Tip amount: ${:.2f}".format (tip_amount))
    print("Total bill: ${:.2f}".format (total_bill))
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
