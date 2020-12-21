my_list=[1,2,3,7,9]

def iterative_even(my_list):
  x=1
  counter=0
  for number in range(3,len(my_list)+1):
    if my_list[x]%(number)!=0:
      counter=counter+1
    x=x+1
  return counter

print(iterative_even(my_list))

# I will study for the recursion and solve them in a proper way
    