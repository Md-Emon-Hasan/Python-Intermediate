# multithreading
print("multithreading:")
import time
from threading import Thread

database_value = 0
def increase():
    global database_value
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
if __name__ == "__main__":
    print("start value", database_value)
    thread1 = Thraed(target=increase)
    thread2 = Thraed(target=increase)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("end value"+ database_value)  
    
# multithreading
print("multithreading:")
import time
from threading import Thread, Lock

database_value = 0
def increase(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()
if __name__ == "__main__":
    lock = Lock()
    print("start value", database_value)
    thread1 = Thraed(target=increase, args=(lock,))
    thread2 = Thraed(target=increase, args=(lock,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("end value"+ database_value)
    
# multithreading
print("multithreading:")
import time
from threading import Thread, Lock

database_value = 0
def increase(lock):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        lock.release()
if __name__ == "__main__":
    lock = Lock()
    print("start value", database_value)
    thread1 = Thraed(target=increase, args=(lock,))
    thread2 = Thraed(target=increase, args=(lock,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("end main")
    
# multithreading with queue
print("multithreading with queue:")
import time
from threading import Thread, Lock
from queue import Queue

if __name__ == "__main__":
    Q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    first = q.get()
    print(first)
    q.task_done()
    q.join()
    print("end main")

# multithreading with queue
print("multithreading with queue:")
import time
from threading import Thread, Lock
from queue import Queue

def worker(q):
    while True:
        value = q.get()
        '''processing'''
        print(f"in {current_thread().name} got {value}")
        q.task_done()
if __name__ == "__main__":
    Q = Queue()
    run_threads = 10
    for i in range(run_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = True
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()        
    print("end main")
    
    
# multithreading with queue
print("multithreading with queue:")
import time
from threading import Thread, Lock
from queue import Queue

def worker(q):
    while True:
        value = q.get()
        '''processing'''
        print(f"in {current_thread().name} got {value}")
        q.task_done()
if __name__ == "__main__":
    Q = Queue()
    run_threads = 10
    for i in range(run_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = True
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()        
    print("end main")
    
# multithreading with queue
print("multithreading with queue:")
import time
from threading import Thread, Lock
from queue import Queue

def worker(q):
    while True:
        value = q.get(q, lock)
        '''processing'''
        print(f"in {current_thread().name} got {value}")
        q.task_done()
if __name__ == "__main__":
    Q = Queue()
    lock = Lock()
    run_threads = 10
    for i in range(run_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()        
    print("end main")
    
# multithreading with queue
print("multithreading with queue:")
import time
from threading import Thread, Lock
from queue import Queue

def worker(q):
    while True:
        value = q.get(q, lock)
        '''processing'''
        print(f"in {current_thread().name} got {value}")
        q.task_done()
        if ...:
            break
if __name__ == "__main__":
    Q = Queue()
    lock = Lock()
    run_threads = 10
    for i in range(run_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = False
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()        
    print("end main")