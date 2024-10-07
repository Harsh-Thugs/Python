class Dog: #Class
   def __init__(self,name,age): #Constructor
     self.name = name #Attribute
     self.age = age 
   def bark(self): #Method
     return f"{self.name} is barking"
my_dog = Dog("Sheru",2) #Object(intsance of dog)
print("Name: ",my_dog.name)
print("Age: ",my_dog.age)
print(my_dog.bark())
