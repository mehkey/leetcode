'''
101

010

000

011

001


101

111  ( 010)

010

011

010


'''


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        sol = [0] * len(pref)
        
        acc = [0] * len(pref)
        acc[0] = pref[0]
        for i in range(1,len(pref)):
            acc[i] = acc[i-1]

        #print(sol)

        sol[0] = pref[0]
        cur = pref[0]
        acc[0] = pref[0]
        n = cur
        
        for i in range(1,len(pref)):
            n = pref[i-1]^pref[i]#pref[i-1] | pref[i] & ~(pref[i-1]&pref[i])
            
            sol[i] = n
            

        return sol