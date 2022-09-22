#decorators using logging
import logging
# create file to store logging info
# logging is writing status msgs to a file, where file contains which part of
# code is executed and what errors are there.
logging.basicConfig(filename='exampl1.log',level=logging.INFO)  #all events above info gets logged

def outer(func):
    def inner(*args):
        logging.info('Running {} with {}'.format(func.__name__,args))
        print(func(*args))
    return inner

def add(x,y):
    return x+y

obj =  outer(add)
obj(4,5)
