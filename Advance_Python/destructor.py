import gc
import time
import sys

class time:
    def __init__ (self):
        print("Contructor is called ")
        
    def __del__ (self):
        print("Destructor is called ")
        
t=time()
t=None

print(" ------------------------------------")


