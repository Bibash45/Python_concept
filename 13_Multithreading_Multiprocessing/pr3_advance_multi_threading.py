## Multithreading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number: {number}"

numbers=[1,2,3,4,5,9,3902,3298,32,32,2]
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)
    
for result in results:
    print(result)