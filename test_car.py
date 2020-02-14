import unittest
from car import car

class TestCar(unittest.TestCase):

    def test_initalization(self):
        car1 = car()
        self.assertEqual(car1.name, 'Ferari')
        self.assertEqual(car1.color, '')
        self.assertEqual(car1.speed, 33)

        car2 = car(name='car2', color='Red', speed=100)
        self.assertEqual(car2.name, 'car2')
        self.assertEqual(car2.speed, 100)
        self.assertEqual(car2.color, 'Red')
    

if(__name__ == '__main__'): unittest.main()
