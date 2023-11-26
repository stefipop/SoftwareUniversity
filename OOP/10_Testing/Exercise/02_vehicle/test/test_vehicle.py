from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
    
    def setUp(self):
        self.car = Vehicle(50, 100)
    
    def test_correct_initialization(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(100, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(50, self.car.capacity)
    
    def test_drive_insufficient_fuel(self):
        with self.assertRaises(Exception) as e:
            self.car.drive(kilometers=100)
        self.assertEqual("Not enough fuel", str(e.exception))
    
    def test_drive_sufficient_fuel(self):
        self.car.drive(40)
        self.assertEqual(0, self.car.fuel)
    
    def test_refuel_exceeds_capacity(self):
        # self.car.drive(30)
        with self.assertRaises(Exception) as e:
            self.car.refuel(38)
        self.assertEqual("Too much fuel", str(e.exception))
    
    def test_refuel_within_capacity(self):
        initial_fuel = self.car.fuel
        self.car.drive(30)
        self.car.refuel(30)
        expected_fuel = initial_fuel + 30 - 30 * self.car.fuel_consumption
        self.assertEqual(expected_fuel, self.car.fuel)
    
    def test_str_representation(self):
        expected = (f"The vehicle has {self.car.horse_power} horse power with"
                    f" {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption")
        self.assertEqual(expected, str(self.car.__str__()))


if __name__ == '__main__':
    main()
