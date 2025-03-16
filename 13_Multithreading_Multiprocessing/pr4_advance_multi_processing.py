## Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"{number * number}"

numbers=[1,2,3,4,5,9,3902,0,32,32,2]

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)