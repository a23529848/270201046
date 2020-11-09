list=[8,60,43,55,25,134,1]
sumOfThem=0
for elements in range(len(list)):
  print(f"adding element..:{list[elements]}")
  sumOfThem=int(list[elements])+sumOfThem
  print("Total="+str(sumOfThem))
  print("*")