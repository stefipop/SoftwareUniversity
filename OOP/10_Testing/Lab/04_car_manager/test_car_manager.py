from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Camry", 8, 60)
    
    def test_correct_initialization(self):
        self.assertEqual("Toyota", self.car.make)
        self.assertEqual("Camry", self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)
    
    def test_invalid_make(self):
        with self.assertRaises(Exception) as e:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(e.exception))
    
    def test_invalid_model(self):
        with self.assertRaises(Exception) as e:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(e.exception))
    
    def test_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(e.exception))
    
    def test_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(e.exception))
    
    def test_invalid_fuel_amount(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(e.exception))
    
    def test_refuel_success(self):
        self.car.refuel(64)
        self.assertEqual(60, self.car.fuel_amount)
    
    def test_refuel_negative_amount(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))
    
    def test_drive_success(self):
        self.car.refuel(40)
        self.car.drive(500)
        self.assertEqual(0, self.car.fuel_amount)
    
    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as e:
            self.car.drive(800)
        self.assertEqual("You don't have enough fuel to drive!", str(e.exception))


if __name__ == "__main__":
    main()
