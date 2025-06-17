class Car:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand

    def accelerate(self):
        print("Car is racing....")


car1 = Car(220, "BMW")
print(f"{car1.brand} has top speed of {car1.speed}mph")
car1.accelerate()