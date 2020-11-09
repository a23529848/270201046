for i in range(3):
  print(i)
  print("Hello World")

print("\n"+"*"*13+"\n")
###############################################################
for x in range(0,6,2) :
  print(x)
  print("Hello Mars")
###############################################################
list=["a","b","c"]
  
print("*"*13+"\n")

for list_p in list:
  print(list_p)

print("\n"+"*"*13+"\n")
###############################################################
name="Berke"

for ch in name:
  print(ch)

print("\n"+"*"*13+"\n")
###############################################################
for ch_n in range(len(name)):
  print(name[ch_n])
  if ch_n==1 :
    break
###############################################################
print("\n"+"*"*13+"\n")
for ch_n in range(len(name)):
  if ch_n==1 :
    continue
  print(name[ch_n])