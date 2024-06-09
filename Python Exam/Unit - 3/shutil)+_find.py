import shutil as sh

cmd = "pp_file.txt"

path = sh.which(cmd)

print(path)