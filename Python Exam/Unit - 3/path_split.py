import os

path = "\mohit\kumar\hello.txt"

dir_name, file_name = os.path.split(path)
print(dir_name)
print(file_name)