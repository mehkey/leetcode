class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(":")
        #print(s)
        #print(ord(s[0][0]))
        #print(ord(s[0][0]) - ord('A'))
        #print(ord(s[1][0]) - ord('A'))
        res = []
        for i in range(ord(s[0][0]) - ord('A'),ord(s[1][0]) - ord('A')+1):
            for j in range(int(s[0][1]),int(s[1][1])+1):
                res.append( chr(i + ord('A')) + str(j))
        
        #print(res)
        return res