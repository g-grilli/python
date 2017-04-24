text = input("Text? ")
size = len(text)
count = 0
while count < 4:
    if count == 0 or count == 2:
        print((size + 4) * "*")
        count += 1
    elif count == 1:
        print("* " + text + " *")
        count += 1
    else:
        break
