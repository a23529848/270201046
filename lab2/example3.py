normal_price=3

age=int(input("Please print your age"))

if age > 60 and age < 6 :
  normal_price="Free"
elif age<18 :
  normal_price=normal_price-normal_price*(50/100)

print("You can enter with",normal_price)
