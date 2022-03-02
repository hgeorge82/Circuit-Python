class Dog:
     kind = "canine" # class variable shared by all instances
     
     # you don't need an __init__ method, but it is common for stuff that runs at instantiaion
     def __init__(self, breed, age):
          self.breed = breed # instance variable unique to each instance
          self.age = age
          self.tricks = []

     # let's define two methods, addTrick and bark
     def addTrick(self, trick):
          self.tricks.append(trick)

     def bark(self):
          return "arf"