class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        
        prices.sort()
        
        mid = money // 2
        
        for i in range(len(prices)-1):
            if prices[i] + prices[i+1] <= money:
                return money - prices[i] - prices[i+1]

        return money