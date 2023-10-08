from threading import *
import time
l=Lock()
def play(name):
    l.aquire()
    for i in range (10):
        print("Batting : ",name)
        time.sleep(l)
    l.release()
    
t1=Thread(target=play,args=("sachin",))
t2=Thread(target=play,args=("Yuraj",))
t3=Thread(target=play,args=("Kohli",))

t1=start()
t2=start()
t3=start()
