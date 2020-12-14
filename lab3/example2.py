gpa=float(input("Please type your gpa="))

num_of_lectures=int(input("Please type number of your lectures="))

if gpa>2.0 and num_of_lectures>47 :
  print("Graduated!!!")
elif num_of_lectures<47 :
  print("Your number of lectures not enough to graduate")
elif gpa<2.0 :
  print("Your gpa not enough to graduate")
else :
  print("Your both number of lectures and gpa not enough to graduate")
