from random import randint
password=input("Please enter your password:")
alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guess=""

while guess!=password.lower():
  guess=""
  for _ in range(len(password)):
    guess_letter=alphabet[randint(0,25)]
    guess=guess_letter+guess
  print(guess)