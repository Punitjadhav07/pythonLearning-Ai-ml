class Car :
    # brand = None 
    # model = None
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullname(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        # self.brand = brand
        # self.model = model
        #here we use super() to call the __init__ method of the parent class Car
        super().__init__(brand,model)
        self.batterysize = batterysize


mycar = Car("Toyota","Corolla")
print(mycar.brand)
print(mycar.model)
print(mycar.fullname())

tesla= ElectricCar("Tesla","Model S","100 kWh")
print(tesla.brand)
print(tesla.model)      
print(tesla.batterysize)
print(tesla.fullname())
