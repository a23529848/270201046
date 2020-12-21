def harmonic_iterative(n):
  total=0
  for i in range(1,n+1):
    total=total+ n/(n*i)
  return total
print(harmonic_iterative(5))





def harmonic_recursive(n):
  if n==1:
    return 1
  else:
    return harmonic_recursive(n-1) + 1 / n

print(harmonic_recursive(5))