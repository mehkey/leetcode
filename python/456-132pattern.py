class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        stack = []
        s3 = float("inf")
        for n in nums:
            if n > s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False