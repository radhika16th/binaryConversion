user = input("enter the binary number: ")
binary = user[::-1]
number = 0

for i in range(0, len(binary)):
  if binary[i] == "1":
    number += 2 ** i

print(number)
