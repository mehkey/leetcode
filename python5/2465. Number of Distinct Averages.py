class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        h1 = nums.copy()
        
        h2 = [-i for i in nums.copy()]
        
        ans = set()
        
        heapify(h1)
        heapify(h2)
        
        while h1 and h2:

            n1 = heappop(h1)
            n2= - heappop(h2)

            ans.add(mean([n2,n1]))

        return len(ans)