class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        """res = []
        ac = list(itertools.accumulate(nums.sort()))
        
        for i in range(len(queries)):
            res.append(bisect.bisect(ac, queries[i]))
        return res
        """
        #res = []
        #ac = list(itertools.accumulate(nums.sort()))
        #for i in range(len(queries)):
        #    res.append(bisect.bisect(ac, queries[i]))
        #nums.sort()
        
        ac = list(itertools.accumulate(sorted(nums)))
        return [bisect.bisect(ac, queries[i]) for i in range(len(queries))]
