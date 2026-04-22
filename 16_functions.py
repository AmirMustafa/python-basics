def func(x, y, z = None):
    print(z)
    return x * y, x + y

res1, res2 = func(5, 6)
res3, res4 = func(5, 6, 8)
print(res1, res2)
print(res3, res4)


# def func(x, y):
#     return x * y, x + y

# res1, res2 = func(5, 6)
# print(res1, res2)


# def func(x, y):
#     print("Run", x, y)
#     return x * y

# x = func(5, 6)
# print(x)

# def func():
#     print('run')
#     def func2():
#         print('run 2')
#     func2()
# func()


# def func():
#     print('run')

# func()