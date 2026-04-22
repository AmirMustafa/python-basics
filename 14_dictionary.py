x = {'key': 4}
y = {'key': [5,4,3]}


x['key2'] = 50
x[100] = 5
x[101] = [1,2,3]

del x['key2']
print(x)

# print(x['key'])
# print('key' in x)
# print(list(x.values()))
# print(list(x.keys()))