print("Please write variables of (a)x'2 + (b)x + (c)equation")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

print(str(a)+"x'2"+"+"+str(b)+"x"+"+"+str(c))
 
discriminant=(b*b)-(4*a*c)

if discriminant>0 :
  print("Discriminant="+str(discriminant))
  print("There are two real roots")
elif discriminant==0 :
  print("Discriminant="+ str(discriminant))
  print("There is one real root")
else :
  print("Discriminant="+ str(discriminant))
  print("There are two complex root")
