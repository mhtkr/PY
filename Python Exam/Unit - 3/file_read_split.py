with open("file.txt") as file:
    data = file.readlines()

    for line in data:
        word = line.split()
        print(word)

