class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        hm1 = set()
        hm2 = set()
        
        result = []
        
        for i in range(len(A)):
            hm1.add(A[i])
            hm2.add(B[i])

            result.append( len(hm1 & hm2) )

        return result
