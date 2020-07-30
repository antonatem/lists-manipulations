import unittest
from twoSums import two_nums_sum

class testTwoSum(unittest.TestCase):
    def test_two_nums_sum(self):
        nums = [2, 7, 11, 15]
        target = 9

        ind = two_nums_sum(nums, target)

        self.assertEqual(ind, [0, 1])
