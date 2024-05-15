#Experiment - 5b
s = input("Enter a string - ")

print("Original String - ")
for i in range (0,len(s)):
  print(s[i], end="")

print("\nReversed String - ")
for j in range (len(s)-1, -1, -1):
  print(s[j], end="")
