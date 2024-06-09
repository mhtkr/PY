import shelve

file = shelve.open('shelf')

print(list(file.keys()))

del file['Numbers']

print(list(file.keys()))

file.close()