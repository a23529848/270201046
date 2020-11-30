it=1
how_many=int(input("How Many Student"))
while int(it)!=int(how_many):
  print("For Student"+str(it))
  mid1=int(input("Mid Term 1:"))
  mid2=int(input("Mid Term 2:"))
  fin=int(input("Final:") )
  how_many=how_many-1
  grades=[mid1,mid2,fin]
  avg=mid1*0.3+mid2*0.3+fin*0.4
  print("Student AVG:"+str(avg))
  it=it+1

  


