import unittest
from main import *


class TestMain(unittest.TestCase):
	def test_get_direction(self):
		self.assertEqual(get_direction(-1), 'LEFT');
		self.assertEqual(get_direction(0), 'BALANCED');
		self.assertEqual(get_direction(1), 'RIGHT');


class TestPositionCorrector(unittest.TestCase):
	def test_correct_with_nonzero_position(self):
		starting_pos = 10
		result = PositionCorrector.correct(starting_pos)
		diff = abs(result - starting_pos)

		# at least one correction has to be made
		self.assertNotEqual(result, starting_pos)
		# difference between input and output values has to be within range <1,15>
		self.assertTrue(1 <= diff <= 15)

	def test_correct_with_zero_position(self):
		starting_pos = 0
		result = PositionCorrector.correct(starting_pos)
		diff = abs(result - starting_pos)

		# no corrections should be made
		self.assertEqual(result, starting_pos)


class TestRandomChanger(unittest.TestCase):
	def test_change(self):
		starting_pos = 10
		result = RandomChanger.change(starting_pos);
		# position can change only within range <-15,15>
		self.assertTrue(starting_pos - 15 <= result <= starting_pos + 15)


if __name__ == "__main__":
	unittest.main()
