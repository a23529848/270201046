#factorial

f_number=int(input("Type a Number:"))
mult=1

for n in range(1,f_number+1):
  mult=mult*n
print(f"Factorial : {mult}")