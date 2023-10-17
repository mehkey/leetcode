class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        
        vv = [ [i,len(list(v))] for i,v in groupby(nums)]

        t = 0
        
        for k,v in vv:
            if v == 1:
                return -1
            #elif v == 2:
                #t += 1
            #elif v == 3:
                #t += 1
            elif v % 3 == 0:
                t += v // 3
            else:
                t += v // 3 + 1
            #elif v % 3 == 1:
                #t += v // 3 + 1
        
        return t