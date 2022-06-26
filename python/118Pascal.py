class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        cur = [1]
        
        res.append(cur)
        
        for i in range(numRows-1):
            n = []
            for j in range(len(cur)+1):
                if j == 0 or j == len(cur):
                    n.append(1)
                else:
                    n.append(cur[j]+cur[j-1])

            cur = n
            res.append(cur)

        return res