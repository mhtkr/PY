import pprint as pp

d = {
    'age': 30,
    'children': [{'age': 10,
                  'name': 'Bob'},
                 {'age': 8,
                  'name': 'Charlie'}],
    'name': 'Alice',
    'pets': {'cat': 'Whiskers',
             'dog': 'Fido'}
    }

data = pp.pformat(d, width=20, indent=10)

with open('pp_file.txt', 'w') as file:
    file.write(data)
    file.close()


with open('pp_file.txt') as file:
    print(file.read())

