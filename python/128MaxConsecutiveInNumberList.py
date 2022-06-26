class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        
        100 4 200 3 2
        
        2 3 4.  100.  200
        
        Brute Force O(n 2)
        
        sort (nlog(n))
        
        O(n)
        
        
        """
        
        m = 0
        
        hs = set()
        
        for i in nums:
            hs.add(i)
        
        for i in nums:
            if i - 1 in hs:
                continue
            else:
                count = 1
                while i + count in hs:
                    count += 1
                m = max(count,m)
        
        return m
                
                