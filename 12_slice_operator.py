x = [5, 12, 8, 21, 3, 17, 9, 30]
names = ["Amir", "Rahul", "Sneha", "John", "Fatima", "Amit", "Sara"]

sliced = x[0: 4: 2]  # will print from 0 to 4(excluding 4)
sliced2 = x[:4]  # start at index 0 end at index 4 (excluding 4)
sliced3 = x[1:]  # start at index 1 end at last index (excluding last)

print(sliced2)
print(sliced3)


# sliced2 = x[start: stop]
# sliced3 = x[start: stop: step]