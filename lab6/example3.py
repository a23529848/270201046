st_n=int(input("How many student:"))
listst=[]
for _ in range(1,4):
   list1=[]
   print("For",_,".student")
   e1=int(input("Exam1:"))
   e2=int(input("Exam2:"))
   fn=int(input("Final Score:"))
   list1=[e1,e2,fn]
   listst.append(list1)
   n1=e1*0.3+e2*0.3+fn*0.4
   print(n1)
   if n1>90:
       print("AA")
print(listst)