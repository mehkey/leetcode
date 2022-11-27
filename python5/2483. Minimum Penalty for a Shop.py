class Solution:
    def bestClosingTime(self, customers: str) -> int:

        N = len(customers)

        minpen = float('inf')
        ind = -1

        beforeY = 0
        afterY = customers.count('Y')

        beforeN = 0
        afterN = customers.count('N')

        
        for k in range(N+1):
            

            pen = beforeN  + afterY
            

            if k < N:
                if customers[k] == 'Y':
                    beforeY += 1
                    afterY -= 1
                else:
                    beforeN += 1
                    afterN -= 1
            

            if pen < minpen:
                minpen = pen
                ind = k

        return ind
