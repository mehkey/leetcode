class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        M = len(nums)
        
        N = len(nums[0])
        
        res = []
        
        hm = defaultdict(list)
        
        mm = 0
        for i in range(M):
            for j in range(len(nums[i])):
                hm[i+j].append(nums[i][j])
                mm = max(mm, i+j)
        
        res = []
        for i in range(0,mm+1):
            res.extend(hm[i][::-1])
        
        return res
        '''
        si = i
        sj = 0

        while si >=0:
            if sj < len(nums[si]) :
                res.append(nums[si][sj])

            si -= 1
            sj += 1
        '''
