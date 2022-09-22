# class Dog:
#     # class attribute
#     attr1 = 'mammal'
#
#     def __init__(self,name):
#         self.name = name
#     # driver code
#     # Object Instantiated
# Rodger = Dog('Rodger')
# Tommy = Dog('Tommy')
# # Accessing the class attributes:
# print('Rodger is a {}'.format(Rodger.__class__.attr1))
# print('Tommy is a {}'.format(Tommy.__class__.attr1))
# # Accessing Instance attributes
# print('My name is {}'.format(Rodger.name))
# print('My name is {}'.format(Tommy.name))

#
# class Dog:
#         attr1 = 'mammal'            #class attributes
#         attr2 = 'Dog'
#         def __init__(self,name):
#             self.name = name        #Instance Attributes
#         def fun(self):
#             print(self.attr1)
#             print(self.attr2)
#
# Tomm= Dog('Tomm')
# Rodger = Dog('Rodger')
#
# print(Rodger.attr2)
# print(Tomm.attr1)


class Dog:
    animal = 'Dog'
#     constructor
    def __init__(self,name,color):
        self.name = name
        self.color = color

# Objects of a class
Bunzo = Dog('Bunzo','Black')
Tuffy = Dog('Tuffy','Brown')

print('Bunzo Details:')
print('Bunzo is a',Dog.animal)    #Accessing a class var, as classname.attribute
print('It is',Bunzo.color)        #Accessing instance var, as obj.attribute



#
