x = [5, 12, 8, 21, 3, 17, 9, 30]
names = ["Amir", "Rahul", "Sneha", "John", "Fatima", "Amit", "Sara"]
s = "hello"

sliced4 = x[::-1] # reverse a list
sliced5 = names[::-1] # reverse a list
sliced6 = s[::-1] # reverse a list


sliced6 = (1,2,3,4,5)[::-1] # slice also works in tuples
print(sliced6)
# print(sliced5)
# print(sliced6)


sliced = x[0: 4: 2]  # will print from 0 to 4(excluding 4)
sliced2 = x[:4]  # start at index 0 end at index 4 (excluding 4)
sliced3 = x[1:]  # start at index 1 end at last index (excluding last)

# print(sliced2)
# print(sliced3)


# sliced2 = x[start: stop]
# sliced3 = x[start: stop: step]