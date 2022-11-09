class Solution:
    def totalCost(self, costs: List[int], k: int, c: int) -> int:

        

        N = len(costs)
        cos = [[v,i] for i,v in enumerate(costs)]
        
        h1 = cos[0:c]
        heapify(h1)
        
        if len(costs) >= c *2:
            h2 = cos[N-c:]
        else:
            h2 = cos[len(h1):]
        

        heapify(h2)
        
        
        rest = cos[c:N-c]

        res = 0
        
        h1i = c
        h2i = len(costs) - c
        
        l = 0
        r = len(rest) - 1
        
        while k > 0:
            
            if (h1 and h2 and h1[0][0] <= h2[0][0]) or (not h2 and h1):
                res += h1[0][0]
                heappop(h1)
                if l <= r:
                    heappush(h1, rest[l])
                    l+=1
            elif (h1 and h2) or (not h1 and h2) :
                res += h2[0][0]
                heappop(h2)
                if l <= r:
                    heappush(h2, rest[r])
                    r-=1
            else:
                print("Both Heaps are Empty")
            
            k-= 1
            
        return res

            
        