import unittest
from a_snails_journey import *

class Journey(unittest.TestCase):
    def test_snail_trip (self):
        self.assertEqual(snail_trip(15,1,0.5), 29)

if __name__ == '__main__':
    unittest.main()
