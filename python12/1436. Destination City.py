class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outCount = defaultdict(int)
        
        for s,e in paths:
            outCount[s]+=1
            outCount[e]+=0
        
        for k,v in outCount.items():
            if v == 0:
                return k
        