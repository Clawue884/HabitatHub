import unittest
from habitat.life_support import LifeSupport

class TestLifeSupport(unittest.TestCase):
    def setUp(self):
        self.life_support = LifeSupport()
    
    def test_monitor_oxygen(self):
        self.assertEqual(self.life_support.monitor_oxygen(), 100)
    
    def test_use_water(self):
        self.life_support.use_water(10)
        self.assertEqual(self.life_support.monitor_water(), 90)

if __name__ == "__main__":
    unittest.main()
