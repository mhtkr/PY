import shelve

with shelve.open('shelf') as shelf:

    shelf['Name'] = 'Mohit Kumar'

    print(shelf['Name'])

shelf.close()