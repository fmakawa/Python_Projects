import unittest
from josephus_prob import *

class josephus_problem (unittest.TestCase):
    def test_kill_people(self):
        self.assertEqual(kill_people(5), 3)
        self.assertEqual(kill_people(10), 5)
        self.assertEqual(kill_people(15), 15)



if __name__ == '__main__':
    unittest.main()
