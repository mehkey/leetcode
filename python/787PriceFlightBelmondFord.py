class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        price = [float("inf")] * n
        price[src] = 0

        for i in range(0,k+1):
            #print(price)
            temprice = price.copy()
            for s, e, p in flights:
                if price[s] == float("inf"):
                    continue
                if price[s] + p < temprice[e]:
                    temprice[e] = price[s] + p
            price = temprice

        return price[dst] if price[dst] != float("inf") else -1