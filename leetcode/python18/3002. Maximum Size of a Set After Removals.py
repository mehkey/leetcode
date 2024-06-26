import unittest
from typing import List

from leetcode.python18.3002 import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        nums1 = [1,2,3,4]
        nums2 = [2,3,4,5]
        expected = 4
        result = Solution().maximumSetSize(nums1, nums2)
        self.assertEqual(expected, result)

    def test_example_2(self):
        nums1 = [1,2,3,4,5]
        nums2 = [1,2,3,4]
        expected = 5
        result = Solution().maximumSetSize(nums1, nums2)
        self.assertEqual(expected, result)

    def test_same_sets(self):
        nums1 = [1,2,3]
        nums2 = [1,2,3]
        expected = 0
        result = Solution().maximumSetSize(nums1, nums2)
        self.assertEqual(expected, result)

    def test_empty_sets(self):
        nums1 = []
        nums2 = [] 
        expected = 0
        result = Solution().maximumSetSize(nums1, nums2)
        self.assertEqual(expected, result)

    def test_one_empty_set(self):
        nums1 = [1,2,3]
        nums2 = []
        expected = 3
        result = Solution().maximumSetSize(nums1, nums2)
        self.assertEqual(expected, result)

