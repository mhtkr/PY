n = int(input("Enter the number - "))

fact = 1
for i in range(1,n+1):
  fact = fact*i

print("Factorial of", n, "is", fact)

"Hello" "Python"

#Experiment - 2a
name = input("Enter Your Name - ")
age = int(input("Enter Your Age - "))

if(age > 18 or age == 18):
  print(name, "+You are Eligible for Voting")
else:
  print(name, "You are NOT eligible for Voting")
