year=int(input("Year:"))

if year % 4 == 0 :
  if year %100 ==0 :
    if year %400 != 0:
      print("not leap")
    else:
     print("it is leap a year")
  else:
    print("not leap")
else:
  print("it isnt")