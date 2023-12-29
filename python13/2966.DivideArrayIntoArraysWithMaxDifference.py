class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        cur = nums[0]
        
        arr = []
        ca = []
        for n in nums:
            if len(ca) == 0:
                cur = n
            if n - cur <= k:
                ca.append(n)
                if len(ca) == 3:
                    arr.append(ca)
                    ca = []
                    #cur = n
            else:
                if len(ca) > 0:
                    #arr.append(ca)
                    #ca = []
                    return []
                ca.append(n)
                #cur = n
                
        if len(ca) > 0:
            arr.append(ca)
        return arr