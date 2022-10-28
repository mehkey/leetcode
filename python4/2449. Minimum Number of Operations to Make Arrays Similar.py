class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        '''nums1= sorted(nums)
        target = sorted(target)
        s1 = 0
        s2 = 0
        
        for i,n in enumerate(nums):
            
            d = (target[i] - n) // 2
            #if n < target[i] and abs(target[i] - n) %2 == 0:
            #    s1 += abs(target[i] - n)
            #elif n < target[i] and abs(target[i] - n) %2 == 1:
            #    s1 += abs(target[i] - n) -1
            #    s2 += 1
            if not d: continue
            if d > 0:
                s1 += d

        return s1 #(s1 // 2) + s2
        '''
        
        oddA,evenA=[i for i in nums if i%2],[i for i in nums if i%2==0]
        oddB,evenB=[i for i in target if i%2],[i for i in target if i%2==0]        
        oddA.sort(),evenA.sort()
        oddB.sort(),evenB.sort()
        res=0
        for i,j in zip(oddA,oddB):
            if i>=j: res+=i-j
        
        for i,j in zip(evenA,evenB):
            if i>=j: res+=i-j
        
        return res//2
    
        #oddA,evenA=[i for i in A if i%2],[i for i in A if i%2==0]
        #oddB,evenB=[i for i in B if i%2],[i for i in B if i%2==0]        
        #oddA.sort(),evenA.sort()
        #oddB.sort(),evenB.sort()
        #res=0
        #for i,j in zip(oddA,oddB):
        #    if i>=j: res+=i-j
        
        #for i,j in zip(evenA,evenB):
        #    if i>=j: res+=i-j
        
        #return res//2