normal_price=3

age=int(input("Please print your age:"))

if age > 60 or age <6 :
  normal_price=0
elif age<18  :
  normal_price=normal_price-normal_price*(50/100)

print("You can enter with",normal_price)
