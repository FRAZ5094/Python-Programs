import time 
import multiprocessing

start=time.perf_counter()

def do_something(seconds):
    print("Sleeping for {} second(s)...".format(seconds))
    time.sleep(seconds)
    print("Done sleeping...")

if __name__=="__main__":

    processes=[]

    for _ in range(10):
        p=multiprocessing.Process(target=do_something,args=[1.5])
        p.start()
        processes.append(p)s

    for process in processes:
        process.join()

    finish=time.perf_counter()

    print("Finished in {} second(s)".format(round(finish-start,2)))