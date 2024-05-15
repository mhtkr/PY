#Experiment - 4
n = int(input("Enter the number of elements - "))
num = []

for i in range(0, n):
  ele = int(input())

  num.append(ele)

print("List before sorting - ",num)

num.sort()

print("List after sorting - ",num)
