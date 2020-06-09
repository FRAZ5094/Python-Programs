import time
import concurrent.futures

start= time.perf_counter()

def do_something(seconds):
    print("Sleeping {} second(s)...".format(seconds))
    time.sleep(seconds)
    return "Done sleeping...{}".format(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
    #f1=executor.submit(do_something,1) #scheduels a methods to be executed, returns a future object
    #future object allows a check in on the function execution
    #print(f1.result()) #prints the return value for the function

    secs=[5,4,3,2,1]
    #results=[executor.submit(do_something,1) for sec in range(10)] #creates a list of 10 threads

    results=[executor.submit(do_something,sec) for sec in secs] #creates a list of all args from secs list 
    for f in concurrent.futures.as_completed(results):
        print(f.result())



"""
threads=[]

for _ in range(10): #_ is a doorway variable
    t=threading.Thread(target=do_something,args=[1.5]) #args specifies the argument for the function
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
"""


finish=time.perf_counter()

print("Finsihed in {} seconds".format(round(finish-start,2)))