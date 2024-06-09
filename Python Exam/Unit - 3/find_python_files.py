import os

if __name__ == "__main__":
    pyfiles = [file for root, dirs, files in os.walk('.', topdown=True)
               for file in files if file.endswith(".py")]

    print("Python files - ")

    for file in pyfiles:
        print(file)