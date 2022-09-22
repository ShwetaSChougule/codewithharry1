#Object Serialization and deserialization :

# The process of writing state of the object to a file is called pickling(serialization/marshelling).
# The process of reading state of object from file is unpickling.
# code with harry
import pickle
# cars = ['audi','tata','BMW']     #we have to store this object into file
# file = 'car.pkl'
# f = open(file,'wb')
# pickle.dump(cars,f)
# f.close()

# unpickiling
f = 'car.pkl'
file = open(f,'rb')
cars = pickle.load(file)
print(cars)






