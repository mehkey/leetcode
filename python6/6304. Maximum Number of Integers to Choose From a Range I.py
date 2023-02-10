class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        
        c = 0
        
        i = 1
        
        s = 0
        
        for i in range(1,n+1):
            
            if i not in banned:

                if s +i > maxSum:
                    return c
                c+=1
                s+=i

        return c