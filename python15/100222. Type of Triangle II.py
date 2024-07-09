class Solution:
    def triangleType(self, nums: List[int]) -> str:

        s1 = nums[0]#abs(nums[0]-nums[1])
        s2 = nums[1]#abs(nums[1]-nums[2])
        s3 = nums[2]#abs(nums[2]-nums[0])

        if s1 + s2 > s3 and s1 + s3 > s2 and s3 + s2 > s1:
            pass
        else:
            return "none"

        if s1 == s2 == s3:
            return "equilateral"

        if s1 == s2 or s2 == s3 or s1 == s3:
            return "isosceles"

        return "scalene"