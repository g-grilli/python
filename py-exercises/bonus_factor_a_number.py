nums = int(input("Factor what number ? "))
for i in range(1, nums + 1):
    if nums % i == 0:
        print(i)
