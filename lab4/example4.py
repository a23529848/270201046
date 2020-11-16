
password="abc123"
guess=""
while password!=guess:
  guess=str(input("Please ENTER YOUR PASSWORD="))
  if guess=="help":
    print(password[0])
  elif guess!=password:
    print("wrong")

print("Welcome!")