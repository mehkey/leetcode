class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)

        left = 0

        max_culsters = 0
        
        an = 0
        
        number = 0

        queue = deque()

        for right in range(n):

            while queue and queue[-1][0] < nums[right]:
                queue.pop()

            queue.append((nums[right],right))
            
            #print("number:",nums[right])
            
            if an == 0:
                an = nums[right]
            else:
                an = an & nums[right]
            #print("an:",an)
            
            number += 1

            while True:
                if left > right:
                    break

                if an >= queue[0][0]:
                    #print("here:", an)
                    max_culsters = max(max_culsters,number)
                    break
                else:
                    #print("there:", an)
                    number -= 1
                    #an = queue[0][0]
                    left += 1
                    #print("there:", an)
                    if queue and left> queue[0][1]:
                        queue.popleft()
                    
                    if not queue:
                        an = 0
                    #else:
                       # an = queue[0][0]

        return max_culsters
