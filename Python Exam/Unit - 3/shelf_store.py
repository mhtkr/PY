import shelve

with shelve.open('shelf') as shelf:

    shelf['Name'] = 'Mohit'

    a = [1,3,4,6,7]

    shelf['Numbers'] = a

shelf.close()