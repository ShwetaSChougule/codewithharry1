
# Difference between Multiprocessing and Multithrading:
# Both are used to increase computing power of a system
# Multiprocessing is the system that has more than 1 or 2 processes.ie. CPUs are added for
#                 increasing computing time.
# Multithreading is a system in which multiple threads of same process  are created
#                   for increasing computing speed.

# What is a thread:
# Thread is a sequence of instructions within a program that can be executed independantly of other code.


# Thread lifecycle:
# Pending

# To print current executing thread
# import threading
# print('Current thread is',threading.current_thread().name)


# Three ways of creating thread in python
#  1.Creating thread without any class:
# from threading import *
# def display():
#     for i in range(1,11):
#         print('Child Thread')
#
# t=Thread(target=display)
# t.start()
# for i in range(1,11):
#     print('Main Thread')

# 2.creating Thread by extending thread class

# from threading  import *
# class my(Thread):
#     def run(self):
#         for i in range(1,10):
#             print('Child')
#
# t=my()
# t.start()
#
# for i in range(1, 10):
#     print('main')


# 3.without extending thread class
#
# from threading import *
# class Test:
#     def dis(self):
#         for i in range(1,10):
#             print('Child')
#
# obj=Test()
# t=Thread(target=obj.dis)
# t.start()
#
# for i in range(1, 10):
#     print('main')


# from threading import *
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# doubles(numbers)
# squares(numbers)
# print("The total time taken:",time.time()-begintime)



# from threading import *
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:", n * n)
#
# numbers = [1, 2, 3, 4, 5, 6]
# begintime = time.time()
# t1 = Thread(target=doubles, args=(numbers,))
# t2 = Thread(target=squares, args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The total time taken:", time.time() - begintime)



# # Time taken by threading is less than normal function.
# import threading
# import time
# #
# def do_sleep():
#     print('Before sleeping')
#     time.sleep(1)
#     print('After sleeping')
#
# start = time.time()
# do_sleep()
# do_sleep()
# end= time.time()
#
# print(end-start)


import threading
import time

def do_sleep():
    print('Before sleeping')
    time.sleep(1)
    print('After sleeping')
    print(threading.active_count())



t1 = threading.Thread(target=do_sleep)
t2 = threading.Thread(target=do_sleep)

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end= time.time()
print(threading.active_count())
print(end-start)
