name = input("Enter Your Name - ")
age = int(input("Enter Your Age - "))

if(age > 18 or age == 18):
  print(name, "+You are Eligible for Voting")
else:
  print(name, "You are NOT eligible for Voting")
