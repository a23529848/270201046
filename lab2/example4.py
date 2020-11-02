month=float(input("Please Enter Which Month Want You Book"))
day=int(input("Please Enter Which Day Want You Book"))
month_day=month+day/100 

if 3.20<=month_day<6.20 :
  print("Season  Spring")
elif  6.21<=month_day<9.21 :
  print("Season Summer")
elif 9.22<=month_day<12.20 :
  print("Season Fall")
elif month_day<3.21 or 12.21<=month_day :
  print("Season Winter")
   

   ## I writed after the lab so it can be wrong

   ## user can write large numbers, but  she or he wouldn't know it,.