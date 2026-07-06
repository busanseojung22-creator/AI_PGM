class Car:
    def _init__(self, made, color, model, price):
        self.made = made
        self.color = color
        self.model = model
        self.price = price

    def set_make(self, make):
        self.make = make
    def get_make(self):
        return self.make
    def __str__(self):
        return f"Car(make={self.make}, color={self.color}, model={self.model}, price={self.price})"
    
class ElectricCar(car):
    def __int__(self, make, model, color, price, bettery_capacity):
        super.__init__(make, model, color, price)
        self.battery_capacity = bettery_capacity
    def set_bettery_capacity(self, battery_capacity):
        self.battery_capacity = battery_capacity
    def get_bettery_capacity(self):
        return self.battery_capacity
    def __str__(self):
        return f"ElectricCar(make={self.make}, model={self.model}, color={self.color})"


    

            
        