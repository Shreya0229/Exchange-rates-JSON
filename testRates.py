# file to test and show output of the exchangeRates.py code, for mentioned inputs here.

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertEqual(changeBase(201, "INR", "INR", "2016-10-25"), 201.0)
		self.assertAlmostEqual(changeBase(201, "INR", "INR", "2016-10-25"), 201.0, delta = 0.1)
		
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.
		self.assertEqual(changeBase(0, "INR", "ZAR", "2018-10-25"), 0.0)
		self.assertAlmostEqual(changeBase(0, "INR", "ZAR", "2018-10-25"), 0.0, delta = 0.1)

		self.assertEqual(changeBase(1000, "MYR", "USD", "2006-10-01"), 271.1849884)
		self.assertAlmostEqual(changeBase(1000, "MYR", "USD", "2006-10-01"), 271.1, delta = 0.1)

		self.assertEqual(changeBase(99, "RON", "USD", "2009-10-17"), 34.3274800572)
		self.assertAlmostEqual(changeBase(99, "RON", "USD", "2009-10-17"), 34.3, delta = 0.1)

		self.assertEqual(changeBase(5, "MYR", "INR", "2014-9-23"), 93.913495554)
		self.assertAlmostEqual(changeBase(5, "MYR", "INR", "2014-9-23"), 93.91, delta = 0.1)



if __name__=='__main__':
	unittest.main()
