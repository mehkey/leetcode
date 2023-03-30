class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        p = 0
        c = 0
        n = []
        
        for i in nums:
            if i >= 0:
                p += i
                c += 1
            else:
                n.append(i)
        
        if p == 0:
            return 0
        
        n.sort(reverse=True)
        #print(n)
        
        #print(p)
        
        for i in n:
            p += i
            
            if p <= 0:
                break

            c += 1

        return c
            