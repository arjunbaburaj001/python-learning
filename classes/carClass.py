class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = int(mileage)

    def drive(self, distance):
        self.mileage += distance
        print(self.mileage)

    def car_info(self):
        return f"{self.make}, {self.model}, {self.year}, {self.mileage}"

car1 = Car("Honda", "Civic", "2007", "500")
car1.drive(500)
print(car1.car_info())