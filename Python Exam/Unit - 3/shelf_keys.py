import shelve

file = shelve.open('shelf')

print(list(file.keys()))

file.close()