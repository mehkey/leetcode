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

        #[0, 1, 3, 50, 75]
        #lower = 0 and upper = 99

        if ( nums[l] - lower ) > 0:
            if (nums[l] - lower > 1 ) :
                res.append(str(lower) + "->" + str(nums[l]-1))
            elif ( nums[l] - lower  == 1 ) :
                res.append(str(lower))

        while l < r:

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

        
    

