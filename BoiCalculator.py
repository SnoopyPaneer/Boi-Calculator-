num1=int(input("Enter your first number: "))
op=(input("Enter your operator: "))
num2=int(input("Enter your second number: "))
if op== "+":
  num3 = num1+num2
  print(num1+num2)
elif op== "-":
 num3 = num1-num2
 print(num1-num2)
elif op=="*":
  num3 = num1*num2
  print(num1*num2)
elif op=="/":
  num3 = num1/num2
  print(num1/num2)
elif op== "^":
  num3 = num1**num2
  print(num1**num2)
else:
  print("Invalid Operator")
