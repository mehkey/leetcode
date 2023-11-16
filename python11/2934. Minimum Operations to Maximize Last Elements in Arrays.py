class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)

        def solve(i,left,right):
            if i == n - 1:
                return 0

            elif nums1[i] <= left and nums2[i] <= right:
                return solve(i+1,left,right)
            elif nums1[i] <= right and nums2[i] <= left :
                return solve(i+1,left,right) + 1 
            else:
                return float('inf')

        s1 = solve(0,nums1[n-1],nums2[n-1])
        s2 = solve(0,nums2[n-1],nums1[n-1]) 

        if s1 == float('inf') and s2 == float('inf'):
            return -1

        return min(s1,s2 + 1)
        
        '''
        def solves(i):
            if i == -1:
                return 0

            m1 = max(nums1)

            m2 = max(nums2)
            
            if m1 == nums1[n-1] and m2 == nums2[n-1]:
                return 0

            #if m1 != nums1[n-1] and m2 != nums2[n-1]:
            #    return float('inf')

            s1 = solve(i-1)
            
            nums1[i] , nums2[i] = nums2[i], nums1[i]
            
            s2 = solve(i-1)
            
            nums1[i] , nums2[i] = nums2[i], nums1[i]
            
            return min(s1, s2 +1 )
            
            
            if m1 != nums1[i]:
                mm = float('inf')
                for j in range(0,i):
                    mm = min(mm, solve)
            
        
        #res = solve(n-1)
        
        #r#eturn res if res != float('inf') else -1

        
        
        @cache
        def dp(i, leftGood, rightGood):

            if leftGood and rightGood:
                return 0
            
            if i == 0:
                return -1

            m1 = max(nums1[0:i])

            m2 = max(nums2[0:i])

            for j in range(0,i):
                if nums[]
        
        m1 = max(nums1)

        m2 = max(nums2)
        
        return dp(n-1,m1 == nums1[n-1], m2 == nums2[n-1] )
        
        n = len(nums1)
        
        m1 = max(nums1)

        m2 = max(nums2)
        
        if m1 == nums1[n-1] and m2 == nums2[n-2]:
            return 0
        '''


