class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Car:", self.make, self.model)

# Creating objects of class Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# Accessing attributes and methods of objects
car1.display_info()  # Output: Car: Toyota Camry
car2.display_info()  # Output: Car: Honda Accord

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print("Electric Car:", self.make, self.model, "- Battery:", self.battery_capacity, "kWh")

# Creating objects of class ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 100)

# Accessing methods of ElectricCar and inherited methods from Car
electric_car.display_info()  # Output: Electric Car: Tesla Model S - Battery: 100 kWh

# Polymorphic function
def display(car):
    car.display_info()

# Using polymorphism to display different types of cars
display(car1)          # Output: Car: Toyota Camry
display(electric_car)  # Output: Electric Car: Tesla Model S - Battery: 100 kWh
