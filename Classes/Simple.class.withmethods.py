class Dog:
    # Class  attribute
    attr1 = 'mammal'
    #Instance attribute
    def __init__(self,name):
        self.name = name     #instance attribute

    def Show(self):
        print('My name is {}'.format(self.name))

#Driver code - Object creation
Zoro = Dog('Zoro')
Tom = Dog('Tom')
#Accessing Class methods
Zoro.Show()
Tom.Show()

