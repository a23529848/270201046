###PART1
def is_prime(number):
  for i in range(2,number):
    if number%i==0:
      return False
    else:
      return True
print(is_prime(7))