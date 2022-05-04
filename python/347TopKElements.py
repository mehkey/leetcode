class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        hashmap = {}
        
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        freq = [[] for i in range(len(nums)+1)]
        
        for n,c in hashmap.items():
            freq[c].append(n)
        
        res = []
        
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        return res
        
        