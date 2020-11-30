 #Aprogram to average a set of numbers
 # Illustrates counted loop with accumulator

print("\nThis Programs Leads You To Find Average Number\n\n"+"*"*60)

n=int(input("How much numbers will you enter? : "))
sum=0
for _ in range(n):
  x=int(input("Enter Your Number:"))
  sum=sum+x
print("The Average Number:"+str(sum/n))


