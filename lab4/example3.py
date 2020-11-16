number1=int(input("Enter a number 1:"))
number2=int(input("Enter a number 2:"))

matches=0

while number1>0 and number2>0:
  if number1%10==number2%10:
    matches=matches+1
  number1=number2//10
  number2=number1//10


print(matches)