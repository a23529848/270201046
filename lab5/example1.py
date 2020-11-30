email=input("Mail:")

email=email.lower()

number_of_at=email.count("@")

before_at=email.split("@")[0]
after_at=email.split("@")[1]

email=before_at.replace(".","")+"@"+after_at



if number_of_at==1:

  if email=="ceng113@example.com":
    print("doğru")

  else:
    print("yanlış")

else:
  print("birden fazla @ yapamazsınız")
