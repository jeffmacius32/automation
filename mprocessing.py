import multiprocessing
import os
import time
import random
from datetime import datetime

def whoami(what):
    # Generate a random sleep time between 0 and 1 seconds
    print("Process %s says: %s" % (os.get(), what))
    
 
 
if __name__ == "__main__":
    # Create three separate processes
    whoami("Im the main program")
    for i in range(4):
        p = multiprocessing.Process(target=whoami, args = ("I'm function %s" % i,))
        p.start()
       
   
