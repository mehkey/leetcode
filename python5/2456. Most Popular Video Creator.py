class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        pop = defaultdict(int)

        pop_small = defaultdict(list)

        for i,creator in enumerate(creators):
            
            pop[creator] += views[i]
            
            heappush(pop_small[creator], [-views[i],ids[i]])
        
        m = max(pop.values())
        
        res = []
        for creator in pop:
            if pop[creator] == m:
                res.append([creator, pop_small[creator][0][1]])

        return res
            