import shutil as sh

source = r"C:\Users\mohit\Desktop\Python Exam\Unit - 3\file.txt"
desti = r"C:\Users\mohit\Desktop\Python Exam\Unit - 3\mohit\kumar\hello.txt"

path = sh.copy(source, desti)

print(path)