# typical example of context meneger
print("typical example of context meneger:")
# with open("notes.txt", "w") as file:
#     file.write("some todoo...")
# file = open("notes.txt", "w")
# try:
#     file.write("some todoo...")
# finally:
#     file.close()

# typical example of context meneger
print("typical example of context meneger:")
# from threading import Lock
# lock = Lock()
# lock.acquire()
# '''....'''
# lock.release()
# with lock:
#     '''....'''
    
# implemnt a context manager for our own classes
print("implemnt a context manager for our own classes:")
# class ManagedFile:
#     def __init__(self, filename):
#         print("init")
#         self.filename = filename
#     def __enter__(self):
#         print("enter")
#         self.file = open(self.filename, "w")
#         return self.file
#     def __exit__(self, exc_type, exc_value, exc_trackback):
#         if self.file:
#             self.file.close()
#             print("exit")
# with ManagedFile("notes.txt") as file:
#     print("do some stuff...")
#     file.write("some todoo...")
    
# implemnt a context manager for our own classes
print("implemnt a context manager for our own classes:")
# class ManagedFile:
#     def __init__(self, filename):
#         print("init")
#         self.filename = filename
#     def __enter__(self):
#         print("enter")
#         self.file = open(self.filename, "w")
#         return self.file
#     def __exit__(self, exc_type, exc_value, exc_trackback):
#         if self.file:
#             self.file.close()
#             print("exc", exc_type, exc_value)
#             print("exit")
# with ManagedFile("notes.txt") as file:
#     print("do some stuff...")
#     file.write("some todoo...")
#     file.somemethod()     
# print("counting")

# implemnt a context manager for our own classes
print("implemnt a context manager for our own classes:")
# class ManagedFile:
#     def __init__(self, filename):
#         print("init")
#         self.filename = filename
#     def __enter__(self):
#         print("enter")
#         self.file = open(self.filename, "w")
#         return self.file
#     def __exit__(self, exc_type, exc_value, exc_trackback):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print("exception has been handle")
#         print("exc", exc_type, exc_value)
#         print("exit")
#         return True
# with ManagedFile("notes.txt") as file:
#     print("do some stuff...")
#     file.write("some todoo...")
#     file.somemethod()     
# print("counting")

from contextlib import contextmanager
@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()
with open_managed_file("notes.txt") as f:
    f.write("some todoo...")