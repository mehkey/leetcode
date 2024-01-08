class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        c = Counter(nums)

        res = 0
        for v in c.values():
            
            if v == 1:
                return -1
            elif v % 3 == 0:
                res += v // 3
            else:
                res += ceil (v/3)
            '''
            elif (v - 2) % 3  == 0:
                res += 1 + (v - 2) // 3
            elif (v - 4) % 3  == 0:
                res += 2 + (v - 4) // 3
            else:
                return -1
            '''

        return res