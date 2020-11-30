import time

minute=int(input("Kaç dakika çalışacaksın ?="))
  
while minute!=0:
  for sec in range(59,-1,-1):
    time.sleep(1)
    print(minute-1,sec)
  minute=minute-1

print("Mola Zamanı!")

  
