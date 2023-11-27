import unittest
from Solution import Solution


class TestModifiedBinarySearch(unittest.TestCase):
    def test_find_element(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        s = Solution()
        find_elem = s.search(nums, target)

        self.assertEqual(find_elem, 4)


if __name__ == "__main__":
    unittest.main()
