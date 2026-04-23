try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')


# raise FileExistsError('File exists!!!!')

# raise Exception('Bad')