###PART1
def is_prime(number):
  for i in range(2,number):
    if number%i==0:
      return False
    else:
      return True
print(is_prime(21))

def between(a,b):
  for n in range(a,b):
    if is_prime(n)==True:
      print(n)
x=int(input("Primes from:"))
y=int(input("to:"))
between(x,y)

