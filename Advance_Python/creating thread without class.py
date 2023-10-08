from threading import *
def show():
    for i in range (1,11):
        print("child Thread")
        
t=Thread(target=show)
t.start()
for i in range (1,11):
    print("Main Thread")
