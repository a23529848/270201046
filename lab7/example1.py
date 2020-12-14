books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict={}
book_dicts={}
for book in books:
  counter=0##SESLİ HARF
  l_counter=0##TÜM HARFLER
  for letter in book:
    l_counter=l_counter+1
    if letter == "A" or letter=="I" or letter=="E" or letter=="U" or letter=="O":
      counter=counter+1
    if letter==" "or letter=="'":
      l_counter=l_counter-1
  uniq=l_counter-counter
  book_dict[book]=(l_counter,uniq)
print(book_dict.keys(),"--->",book_dict.values())

