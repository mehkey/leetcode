class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        hm = defaultdict(int)

        for n in nums:
            
            hm[n] += 1
        
        
        m = 1

        
        for n in nums:
            
            if n == 1:
                m = max(m , hm[n] if hm[n] % 2 == 1 else hm[n]-1 )
                continue
            
            cm = 0
            i = 1

            while True:
                if hm[n ** i] >= 2:
                    cm += 2
                elif hm[ n ** i] == 1:
                    cm += 1
                    m = max(m, cm)
                    break
                else:
                    m = max(m, cm - 1)
                    break
                i *= 2

        return m