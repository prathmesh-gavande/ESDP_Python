from threading import *
print(current_thread().getName())
print(current_thread().setName("Raj"))
print(current_thread().getName())
