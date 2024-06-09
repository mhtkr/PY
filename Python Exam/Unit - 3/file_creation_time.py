import os
import time

t = os.path.getctime('file.txt')
print(time.ctime(t))