def func(x, y):
    print(x,y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    func(*pairs)


# def func(*args, **kwargs):
#     pass

# x = [1, 454, 112, 2, 213213]
# func(x)

# print(*x)
# print(x)