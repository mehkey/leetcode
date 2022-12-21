class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        G = defaultdict(set)
        
        for e in edges:
            G[e[0]].add(e[1])
            G[e[1]].add(e[0])
            
        res = []
        for g in G:
            if len(G[g]) %2 == 1: 
                res.append(g)
        
        if len(res) > 4:
            return False

        if len(res) == 0:
            return True

        if len(res) == 1: 
            return False

        if len(res) == 3 :
            return False

        #2 or 4
        if len(res) == 2:
            if res[1] in G[res[0]] and (len(G[res[0]]) == n-1  or len(G[res[1]]) == n-1):
                return False
            return True

        if len(res) == 4:
            count = 0

            if res[1] in G[res[0]]:
                count += 1
            if res[2] in G[res[0]]:
                count += 1
            if res[3] in G[res[0]]:
                count += 1
            if res[1] in G[res[2]]:
                count += 1
            if res[3] in G[res[2]]:
                count += 1
            if res[1] in G[res[3]]:
                count += 1
            

            if count <= 2:
                return True
            
            if count == 4:
                return True

            return False

        return True
