### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in 'ABCDE':
        time.sleep(2)
        print(f"Letter: {letter}")
        

## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

## start the threads
t1.start()
t2.start()

## wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time()
print(f"Time taken : {finished_time - t}")
