#multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array
# import time
# def add_100(number):
#     for i in range(100):
#         time.sleep(0.01)
#         number.value += 1
# if __name__ == "__main__":
#     shared_number = Value("i",0)
#     print("Number at beginning is", shared_number.value)
#     p1 = Process(target=add_100, args=(shared_number,))
#     p2 = Process(target=add_100, args=[shared_number,])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("number at end is", shared_number.value)

#multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array, Lock
# import time
# def add_100(number):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         number.value += 1
#         lock.release()
# if __name__ == "__main__":
#     lock = Lock
#     shared_number = Value("i",0)
#     print("Number at beginning is", shared_number.value)
#     p1 = Process(target=add_100, args=(shared_number, lock))
#     p2 = Process(target=add_100, args=[shared_number, lock])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("number at end is", shared_number.value)
    
# multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array, Lock
# import time
# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1
# if __name__ == "__main__":
#     lock = Lock
#     shared_number = Value("i",0)
#     print("Number at beginning is", shared_number.value)
#     p1 = Process(target=add_100, args=(shared_number, lock))
#     p2 = Process(target=add_100, args=[shared_number, lock])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("number at end is", shared_number.value)
    
# multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array, Lock
# import time
# def add_100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         for number in numbers:
#             number += 1
# if __name__ == "__main__":
#     lock = Lock
#     shared_array = Array("d", [0.0, 100.0, 200.0])
#     print("array at beginning is", shared_array.value)
#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=[shared_array, lock])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("array at end is", shared_array.value)

# multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array, Lock
# import time
# def add_100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             numbers[i] += 1
# if __name__ == "__main__":
#     lock = Lock
#     shared_array = Array("d", [0.0, 100.0, 200.0])
#     print("array at beginning is", shared_array.value)
#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=[shared_array, lock])
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("array at end is", shared_array.value)

# multiprocessing
print("multiprocessing:")
# from multiprocessing import Process, Value, Array, Lock, Queue
# from queue import Queue
# import time
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)
# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)
# if __name__ == "__main__":
#     numbers = range[1, 6]
#     q = Queue()
#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     while not q.empty():
#         print(q.get())

# process tools multiprocessing
print("process tools multiprocessing:")
# multiprocessing
# from multiprocessing import Process, Value, Array, Lock
# import time
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)
# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)
# if __name__ == "__main__":
#     numbers = range(1, 6)
#     q = Queue()
#     p1 = Process(target=square, args=(numbers, q))
    
#     p2 = Process(target=make_negative, args=(numbers,q))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     while not q.empty():
#         print(q.get())

# multiprocessing
print("multiprocessing:")
# from multiprocessing import Pool, Value, Array, Lock
# def cube(number):
#     return number * number * number
# if __name__ == "__main__":
#     numbers = range(10)
#     pool = Pool()
#     '''map, appaly, join, close'''
#     result pool.map(cube, numbers)
#     print(result)

# multiprocessing
print("multiprocessing:")
from multiprocessing import Pool, Value, Array, Lock
def cube(number):
    return number * number * number
if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()
    '''map, appaly, join, close'''
    result pool.map(cube, numbers)
    pool.close()
    pool.join()
    print(result)

# multiprocessing
print("multiprocessing:")
from multiprocessing import Pool, Value, Array, Lock
def cube(number):
    return number * number * number
if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()
    '''map, appaly, join, close'''
    result pool.map(cube, numbers)
    pool.apply(cube, numbers[0])
    pool.close()
    pool.join()
    print(result)