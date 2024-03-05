# name = ""
# while(name == ""):
#     name = str(input("Enter your name : "))
#     if(name):
#         continue
#     else :
#         print("Please enter your name: ")
# print("Hello " + name)

# for i in range(3):
#     print(i)

# ====================lists ====================
mylist = ["Nepal", "India", "China", "Japan", "USA", "United-Kingdom"]

# for i in mylist: 
#     print(i,len(i))

# for i in range(len(mylist)):
    # print("index: " + str(i) + " value: " + mylist[i])

# creating a list
# nums = list(range(5))
# print(nums)

# find sum
# print(sum(range(5)))




# nested loops 
# for i in range(1,5):
#     for j in range(6,10):
#         print(j)


# cheking for prime number 
# primes= []
# for i in range(2,10):
#     for x in range(2,i):
#         if (i%x == 0):
#             print(i, 'equals', x, '*', i//x)
#             break
#         else:
#             print(i, "is a prime number !")
#             primes.append(i)


# print("Prime numbers : ", list(set(primes)))

add = lambda a, b : a + b
# print(add(1,2))



# def http_err(status):
#     match status : 
#         case 400:
#             return "Bad request"
#         case 404 :
#             return "Not found"
#         case 500 :
#             return "Server error"
#         case _ :
#             return "Invalid Input"
# print(http_err(400))

def greet(name:str, age:int) -> str:
    '''sample function to greet user with their age and name'''
    return f"Hello {name}! you are {age} years old"

docstring = greet.__doc__
print(docstring)
def hello(name:str) -> str:
    return f"hello {name}, welcome to my program"




# print(hello("Sudeep Bogati"))

# ------------------ OOP ---------------------

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"brnad : {self.brand}\nModel : {self.model}"
    
    def accelerate(self):
        return f"Car info : model => {self.model}, brand => {self.brand} "
        # return "Car is accelerating"
    def display_model_and_brand(self):
        print(self.__str__())


car1 = Car("BMW", "X5")
car2 = Car("Nissan", "GTR")
car3 = Car("RR", "Nothing")
# print("First instance of object : ", car1.brand)
# print("Second instance of car Object : ", car2.accelerate())
# car3.display_model_and_brand()

class Animal:
    pass
    # def speak(self):
    #     pass

class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
        
def speaking_of_animals(animal):
    return animal.speak()

cat = Cat()
dog = Dog()

# print(speaking_of_animals(cat))
# print(speaking_of_animals(dog))



# -------static and class methods


class Vehicle:
    class_variable = "This is class variable"
    def __init__(self,name):
        self.vehicle_name = name
    # static methods 
    def wheel(cls):
        print(f"{cls.class_variable}")

    @staticmethod
    def accelerate():
        print("The vehicle is accelerating....")

Vehicle.wheel("Bike")


def greet(name:str, age:int) -> str:
    '''sample function to greet user with their age and name'''
    return f"Hello {name}! you are {age} years old"

docstring = greet.__doc__
print(docstring)




class Rectangle:
    def __init__(self, width:float, height:float) -> None:
        self.width = width
        self.heght = height
    
    def width(self):
        return self.width
    def height(self):
        return self.height
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width + self.height


rect = Rectangle(5,4)

rect.width()