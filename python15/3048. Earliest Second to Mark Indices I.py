class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], ci: List[int]) -> int:
        N = len(nums)
        M = len(ci)
        
        l = N -1
        r = M -1
        res = inf
        
        s = sum(nums)

        if s + len(nums) > len(ci) :
            return -1

        def test(k):
            nums1 = nums[:]

            count = 0
            need = 0
            
            for j in range(k, -1, -1):
                i = ci[j] - 1
                if nums1[i] == -1:
                    if need:
                        need -= 1
                else:
                    need += nums1[i]
                    nums1[i] = -1
                    count += 1
            
            if need == 0 and count == len(nums1):
                return True
            
            return False

        while l <= r:
            
            mid = (l+r) // 2

            if test(mid):
                res = min(res, mid)
                r = mid -1

            else:
                l = mid + 1
        
        return -1 if res == inf else res + 1