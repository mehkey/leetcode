class Solution:

    """
    @param nums: a sorted integer array
    @param lower: An integer
    @param upper: An integer
    @return: a list of its missing ranges
    """
    def find_missing_ranges(self, nums, lower, upper):
        # write your code here

        def getPrint(lower,upper):
            if (upper - lower) > 2 :
                return str(lower) + "->" + str(upper)
            else:
                return str(lower)

        if len(nums) == 0:
            return [getPrint(lower,upper)]

        l = 0

        r = len(nums) - 1

        while l < r and nums[l] < lower :
            l += 1

        while l < r and  nums[r] > upper :
            r -= 1

        res = []

        if ( nums[l] - lower ) > 0:
            if (nums[l] - lower > 1 ) :
                res.append(str(lower) + "->" + str(nums[l]-1))
            elif ( nums[l] - lower  == 1 ) :
                res.append(str(lower))

        while l < r:

            #5 9   -> 6 -> 8
            #5 6   -> ""
            #5 7   -> 6 -> 8

            if ( nums[l+1] - nums[l] > 2 ) :
                res.append(str(nums[l]+1) + "->" + str(nums[l+1]-1))
            elif ( nums[l+1] - nums[l] == 2 ) :
                res.append(str(nums[l]+1))
            l+= 1

        if (upper - nums[l] ) > 0:
            if ( upper - nums[l] > 1 ) :
                res.append(str(nums[l]+1) + "->" + str(upper))
            else:
                res.append(str(upper))

        return res

        
    

class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()