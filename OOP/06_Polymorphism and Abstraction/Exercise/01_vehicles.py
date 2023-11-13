from abc import ABC, abstractmethod


class Vehicle(ABC):
    # Class constant for summer fuel consumption.
    SUMMER_FUEL_CONSUMPTION = 0
    # Class constant for damaged tank.
    TANK_FILLING_CAPACITY = 1

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):
    SUMMER_FUEL_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        consumption = self.fuel_consumption + Car.SUMMER_FUEL_CONSUMPTION
        if self.fuel_quantity >= consumption  * distance:
            self.fuel_quantity -= consumption  * distance

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_CONSUMPTION = 1.6
    TANK_FILLING_CAPACITY = 0.95

    def drive(self, distance: float) -> None:
        consumption = self.fuel_consumption +Truck.SUMMER_FUEL_CONSUMPTION
        if self.fuel_quantity >= consumption  * distance:
            self.fuel_quantity -= consumption  * distance

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.TANK_FILLING_CAPACITY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
