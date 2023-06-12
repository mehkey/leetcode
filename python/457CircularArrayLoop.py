class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        
        
        
        l = len(nums)
        
        for i in range(l):
            if nums[i] == 0:
                return False

            nums[i] = nums[i] % l if nums[i] > 0 else - (l - nums[i] % l)

        for i, num in enumerate(nums):
            visited = set()
            cur = i
            start = i
            visited.add(i)
            
            two = False
            lap = False
            backlap = False
            
            forward = nums[cur] > 0

            while True:

                if forward and nums[cur] < 0:
                    break
                if not forward and nums[cur] > 0:
                    break
                    
                if cur + nums[cur] >=  l:
                    lap = True
                    cur = cur + nums[cur] - l
                elif cur + nums[cur] <  0:
                    backlap = True
                    cur = cur + nums[cur] + l
                else:
                    cur += nums[cur]

                if cur < 0:
                    cur = l + cur
                
                if cur in visited:
                    break

                if cur == start and forward and two and lap:
                    return True

                if cur == start and not forward and two and backlap:
                    return True

                visited.add(cur)
                
                two = True

        return False
