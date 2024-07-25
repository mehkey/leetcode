class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        c = Counter(arr)
        res= len(c.keys())
        for x in sorted(c.keys(), key=lambda x: c[x]):
            if k >= c[x]:
                #c[x]-=1
                k -= c[x]
                res -= 1


        return res 
