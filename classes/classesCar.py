class Car:

    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        if distance > 0:
            self.mileage += distance

    def display_info(self):
        print(f"Car Details: {self.brand}, {self.model}, {self.year}, {self.mileage} (Brand, Model, Year, Mmileage)")

car1 = Car("Ford", "Mustang", "2016", "5000")
car2 = Car("Toyota", "Camry", "2022", "15000")

car1.display_info()
car2.display_info()

car1.drive(250)
car1.display_info()