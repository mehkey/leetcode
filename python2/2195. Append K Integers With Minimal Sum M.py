class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        """"
        nums = set(nums)
        
        res = 0
        
        i = 1
        
        while True:
            
            if i in nums:
                pass
            else:
                res += i
                k-=1
            
            if k ==0:
                break
                
            i+=1
        
        return res
        """
        
        s = nums
        
        t = k * (k+1) // 2
        
        c = k + 1
        
        visited = set()
        #print(Counter(nums))
        ss = set(nums)
        for n in nums:
            if n <= k and n not in visited:
                visited.add(n)
                while c in ss:
                    c += 1
                t += c
                t -= n
                c += 1

        return t
        