count = 0
width = int(input("Width? "))
length = int(input("Length? "))
while count < length:
    count += 1
    if count == 1:
        print(width * '*')
    elif count > 1 and count < length:
        space = width - 2
        empty = space * ' '
        print('*' + empty + '*')
    elif count == length:
        print(width * '*')
