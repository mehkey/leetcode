class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        

        s = 0

        hm = set()

        tt = 0

        for i in range(1, n + 100):

            if k- i in hm:
                pass
            else:
                tt+=1
                s+=i
                hm.add(i)

            if tt == n:
                break
        
        #print(hm)
        return s