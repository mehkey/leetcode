class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        def dist(s,l):
            #print(l)
            res = []
            for i in range(len(s)):
                if s[i] == l:
                    res.append(i)
            return res
        #print(distance)   
        #print(distance)
        #print(len(distance))
        for i in range(len(distance)):
            d = distance[i]
            #print(i, d)
            #print(d-1)
            #if d > 0:
            res = dist(s,chr(i + ord('a')))
            #print(res)
            for i in range(len(res)-1):
                if res[i+1] - res[i] != d +1:
                    return False

        return True
                    