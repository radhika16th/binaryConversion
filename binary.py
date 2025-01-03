number = int(input("enter the number: "))
binary = []

while number != 0:
  quo = number // 2 
  rem = number % 2
  binary.append(rem)
  number = quo

binary.reverse()
print(binary)
