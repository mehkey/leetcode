class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i
        return len(heights) - 1

        N = len(h)

        dis = 0
        b = bricks
        l = ladders

        for i in range(N-1):
            if h[i] >= h[i+1]:
                dis += 1
                continue

            diff = h[i+1] -  h[i]

            if b >= diff:
                b -= diff
            else:
                if l > 0:
                    l -= 1
                else:
                    return dis 
            dis += 1
        
        return dis


        '''
        @cache
        def dp(i,b,l):
            if i == N - 1:
                return 0

            if h[i] >= h[i+1]:
                return dp(i+1,b,l) + 1
            
            dis = 0

            if l > 0:
                dis = max(dis, dp(i+1,b,l-1 ) + 1)

            diff = h[i+1] -  h[i] 

            if  b >= diff:
                dis = max(dis, dp(i+1, b-diff, l ) + 1)
            
            return dis
                

        return dp(0, bricks, ladders)
        '''