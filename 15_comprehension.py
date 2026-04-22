x1 = [x1 for x1 in range(5)]

x2 = [x2 + 5 for x2 in range(5)]

x4 = [x4 % 2 for x4 in range(5)]

x3 = [0 for x3 in range(5)]

x5 = [i for i in range(100) if i % 2 == 0]

# x6 = {i:0 for i in range(100) if i % 2 == 0}
x7 = {i for i in range(100) if i % 2 == 0}

# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(x6)
print(x7)