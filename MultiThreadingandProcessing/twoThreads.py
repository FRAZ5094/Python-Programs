import time
import threading


start= time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

t1=threading.Thread(target=do_something) #create thread to execute the target function
t2=threading.Thread(target=do_something) #create another thread, no () next to the function becuase you dont want to execute it right now

t1.start()  #starts the thread
t2.start()

t1.join() #means that it waits for the thread to complete to continue, bascially joining the threads back
t2.join()

finish=time.perf_counter()

print("Finsihed in {} seconds".format(round(finish-start,2)))