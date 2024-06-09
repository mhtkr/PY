import shutil as sh
import os
source = r"C:\Users\mohit\Desktop\Python Exam\Unit - 3\file.txt"
desti = r"C:\Users\mohit\Desktop\Python Exam\Unit - 3\destination"

path = sh.copy2(source, desti)

print(path)

print(os.stat(desti))
print(os.stat(source))