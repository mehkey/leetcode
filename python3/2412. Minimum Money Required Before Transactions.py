class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:

        '''
        transactions.sort(reverse=True, key=lambda x: (-x[0]+x[1]))
        
        m = 0
        c = 0
        for t in transactions:
            #print(t[0])
            #print(c)
            #print(m)
            #print(t[0])
            if c <= t[0]:
                m += t[0] - c + 1
                c += t[0] - c + 1
                
            
            c -= t[0] - t[1]
            #print(m)
        return m
        
        '''
        diff = [max(cost - cashback, 0) for cost, cashback in transactions]
        print(diff)
        max_amt, sumdiff = 0, sum(diff)
        for i in range(len(transactions)):
            max_amt = max(max_amt, sumdiff - diff[i] + transactions[i][0])
            
        return max_amt