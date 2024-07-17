import threading, queue
import time

def washer(dishes, dish_queue):
    for dish in dishes:

        print("wasjing", dish, "dish") 
        dish_queue.put(dish)



def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish, 'dish')  
        time.sleep(10)
        dish_queue.task_done()  

if __name__ == '__main__':
        dish_queue = queue.Queue()
        for i in range(2):
             dryer_thread = threading.Thread(target=dryer, args=(dish_queue))
             dryer_thread.start()

        # dish_queue = mp.JoinableQueue()
        # dryer_proc = mp.Process(target=dryer, args=(dish_queue))
        # dryer_proc.daemon = True
        # dryer_proc.start()


        dishes = ['salad', 'bread', 'entree', 'desert']
        washer(dishes, dish_queue)
        dish_queue.join()