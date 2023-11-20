class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        #n = len(ed)
        
        hm = defaultdict(bool)
        
        #for i in range(n):
            #found = False
            #for j in range(n):
        for i,j in edges:
            if i == j:
                continue

            #if grid[i][j] == 1:
            hm[j] = True
        
        res = -1
        for i in range(n):
            if hm[i] == False:
                
                if res == -1:
                    res = i
                else:
                    return -1
        
        return res
