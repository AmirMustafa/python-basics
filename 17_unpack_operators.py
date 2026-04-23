def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5, one=0, two=2)


# unwrap with dictionary

# def func(x, y):
#     print(x, y)

# func(**{'x': 2, 'y': 5})


# unwrap with lists or tuples
# def func(x, y):
#     print(x,y)

# pairs = [(1,2), (3,4)]

# for pair in pairs:
#     func(*pairs)


# def func(*args, **kwargs):
#     pass

# x = [1, 454, 112, 2, 213213]
# func(x)

# print(*x)
# print(x)