class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        m = 0
        for i in range(k):
            if numOnes > 0:
                m +=1
                numOnes -=1
            elif numZeros > 0:
                numZeros -= 1
            else:
                m-=1
                numNegOnes -= 1
        
        return m