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

------------------------------------------------------------------------------------------------------------------

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
      return f"Hello, my name  is {self.name} and I am {self.age} years old."
person1 = person("Kamlesh",25)
print("Name: ", person1.name)
print("age: ", person1.age)         
print(person1.greet())
