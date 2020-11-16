
even_counter=0
count=int(input("How many numbers?="))

for _ in range(0,count):
  number=int(input("Enter a integer="))
  if number % 2 == 0:
    even_counter+=1
  else:
    continue

print("%",(even_counter/count)*100)