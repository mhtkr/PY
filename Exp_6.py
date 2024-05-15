#Experiment - 6
import math
pi = 3.14

print("1.Area","\n2.Circumference","\n3.Radius(Area is known)")
n = int(input("Select One -"))

if n==1:
  r = float(input("Enter the radius - "))
  area = pi * math.pow(r,2)
  print("Area of Circle is - ", area)

elif n==2:
  r = float(input("Enter the radius - "))
  circum = 2 * pi * r
  print("Circumferece of Circle is - ", circum)

elif n==3:
  ar = float(input("Enter the known Area - "))
  rad = math.sqrt(ar/pi)
  print("Radius of Circle is - ", rad)
