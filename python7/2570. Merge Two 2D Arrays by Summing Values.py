class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        hm = defaultdict(int)
        
        for v in nums1:
            hm[v[0]] += v[1]
            
        for v in nums2:
            hm[v[0]] += v[1]
        
        return sorted([[k,v] for k,v in hm.items()])