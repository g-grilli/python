height = int(input("Enter height: "))

for i in range (0, height):
    print((height-i) * ' ' + ((i + 1) * 2 - 1) * "*")
