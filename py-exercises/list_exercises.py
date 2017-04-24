# 1. Sum The Numbers
nums = [1, 10, 15, 20]
print(sum(nums))

# 2. Largest Number
nums =[12, 36, 1, 65, 22]
print(max(nums))

# 3. Smallest Number
nums =[12, 36, 1, 65, 22]
print(min(nums))

# 4. Even Numbers
def even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(even_num([12, 36, 1, 37, 55, 26, 47, 88, 99]))

# 5. Odd Numbers
def odd_num(l):
    onum = []
    for n in l:
        if n % 2 != 0:
            onum.append(n)
    return onum
print(odd_num([12, 36, 1, 37, 55, 26, 47, 88, 99]))

# 6. Positive Numbers
def positive_number(l):
    pnum = []
    for n in l:
        if n > 0:
            pnum.append(n)
    return pnum
print(positive_number([12, 36, -1, 37, 55, -26, -47, 88, 99]))

# 7. Multiply a list
def multiply_list(nums, fac):
    new_nums = []
    for i in nums:
        for j in fac:
            new_nums.append(i * j)
    return new_nums
print(multiply_list([1, 2, 3, 4], [5]))

# 8. Multiply Vectors
def multiply_vectors(v1, v2):
    m_vec = []
    for a, b in zip(v1, v2):
        m_vec.append(a * b)
    return m_vec
print(multiply_vectors([2, 4, 5],[2, 3, 6]))

# 9 Matrix Addition
def add_vectors(v1, v2, v3, v4):
    a_vec = []
    b_vec = []
    for a, b in zip(v1, v3):
        a_vec.append(a + b)
    for a, b in zip(v2, v4):
        b_vec.append(a + b)
    return a_vec, b_vec
print(add_vectors([1, 3], [2, 4], [5, 2], [1,0]))

# 10 Matrix addition II

# De-Dup
def de_dup(words):
    words.sort()
    i = len(words) - 1
    while i > 0:
        if words[i] == words[i - 1]:
            words.pop(i)
        i -= 1
    return words
print(de_dup(['pickle', 'wombat', 'pickle', 'dude', 'hello']))

# Bonus: Matrix Multiplication
