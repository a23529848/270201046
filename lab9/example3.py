import time

def waiting_Room(seconds):
    if seconds!=0:
        time.sleep(1)
        print(f"{seconds} seconds left")
        return waiting_Room(seconds-1)
    return "Program is gonna stop!!"
print(waiting_Room(3))