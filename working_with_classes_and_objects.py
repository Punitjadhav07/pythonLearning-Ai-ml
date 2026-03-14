class Car :
    # brand = None 
    # model = None
    # __brand = None # private attribute

    total_cars = 0 # class variable to keep track of the total number of cars created
    def __init__(self,brand,model):
        self.__brand = brand # private attribute
        self.__model = model
        Car.total_cars += 1 # increment the total_cars class variable each time a new Car object is created
    

    
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    @property # this is a decorator that allows us to define a method as a property, which means we can access it like an attribute without needing to call it as a method. In this case, we can access the model of the car using mycar.model instead of mycar.get_model()
    def get_model(self):
        return self.__model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod #this is a decorator that indicates that the following method is a static method, which means it can be called on the class itself without needing an instance of the class. Static methods do not have access to instance-specific data (like self) and are typically used for utility functions that are related to the class but do not require access to instance attributes.
    def genral_info():
        return "cars are means of transport"
    

#inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child class or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent class or superclass). The child class can also have its own unique attributes and methods, in addition to those inherited from the parent class. This promotes code reusability and helps to create a hierarchical relationship between classes.   
class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        # self.brand = brand
        # self.model = model
        #here we use super() to call the __init__ method of the parent class Car
        super().__init__(brand,model)
        self.batterysize = batterysize

    def fuel_type(self):
        return "Electricity"


mycar = Car("Toyota","Corolla")
print(mycar.get_brand()) # we can access the private attribute __brand using the getter method get_brand() defined in the Car class
 # mycar.model= "Camry". we cannot access the private attribute __model directly, but we can set it using the setter method set_model() defined in the Car class
print(mycar.get_model) # we can access the private attribute __model using the getter method get_model() defined in the Car class
print(mycar.fullname())
print(mycar.fuel_type()) # we can call the fuel_type method of the Car class, which returns "Petrol or Diesel"
print(Car.genral_info()) # we can call the static method genral_info using the class name Car.genral_info() and passing an instance of Car as an argument

tesla= ElectricCar("Tesla","Model S","100 kWh")
print(tesla.get_brand()) # we can access the private attribute __brand using the getter method get_brand() defined in the Car class
print(tesla.get_model) # we can access the private attribute __model using the getter method get_model() defined in the Car class
print(tesla.batterysize)
print(tesla.fuel_type()) # we can call the fuel_type method of the ElectricCar class, which overrides the fuel_type method of the Car class
print(tesla.fullname())
print(isinstance(tesla,Car)) # we can use the isinstance() function to check if tesla is an instance of the Car class, which returns True because ElectricCar is a subclass of Car
print(isinstance(tesla,ElectricCar)) # we can use the isinstance() function to check if tesla is an instance of the ElectricCar class, which returns True because tesla is an instance of ElectricCar


safari = Car("Safari","Land Cruiser")
print(safari.get_brand())
print(safari.get_model)
print(safari.fuel_type())   # we can call the fuel_type method of the Car class, which returns "Petrol or Diesel" this is polymorphism in action, as the same method name fuel_type() behaves differently based on the object that calls it (Car or ElectricCar)


print(f"Total cars created: {Car.total_cars}") # we can access the total_cars class variable using the class name Car.total_cars