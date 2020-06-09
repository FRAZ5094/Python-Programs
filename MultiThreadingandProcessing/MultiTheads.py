import time
import threading

#multithreading is for I/O bound operations, aka program has to wait for things to happen and CPU isnt doing much

start= time.perf_counter()

def do_something(seconds):
    print("Sleeping {} second(s)...".format(seconds))
    time.sleep(seconds)
    print("Done sleeping...")

threads=[]

for _ in range(10): #_ is a doorway variable
    t=threading.Thread(target=do_something,args=[1.5]) #args specifies the argument for the function
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish=time.perf_counter()

print("Finsihed in {} seconds".format(round(finish-start,2)))