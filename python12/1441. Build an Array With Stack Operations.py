class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        s = []
        opp = []
        ind = 0
        
        for i in range(1,n+1):
            
            opp.append('Push')
            s.append(i)

            if s[-1] != target[ind]:
                s.pop()
                opp.append('Pop')
            else:
                ind += 1
            
            if ind == len(target):
                break

        return opp