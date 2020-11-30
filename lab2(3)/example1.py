x=float(input("Type the first number="))
y=float(input("Type the second number="))
z=float(input("Type the third number="))

if x<=y and x<=z :
  min_num=x
elif y<=z :
  min_num=y
else :
  min_num=z

print("Minimum Number="+str(min_num))



