class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        N = len(basket1)
        
        #sort the input
        b1 = sorted(basket1)
        b2 = sorted(basket2)

        #two pointers
        p1 = 0
        p2 = 0
        
        #Check if the count of each number is not even, return -1
        c = Counter(b1) + Counter(b2)
        for k in c:
            if c[k] %2 !=0:
                return -1
        
        h1 = []
        h2 = []
        
        cost = []

        smalest_number = 0
        
        while p1 < N and p2 < N:
            if smalest_number == 0:
                smalest_number = min(b1[p1],b2[p2])

            if b1[p1] == b2[p2]:

                p1+=1
                p2+=1
                
            elif b1[p1] <= b2[p2]:
                cost.append( b1[p1])
                p1+=2

            else:
                cost.append( b2[p2])
                p2+=2

        while p1 < N:

            cost.append( b1[p1])
            p1+=2
        while p2 < N:

            cost.append( b2[p2])
            p2+=2

        tot = 0
        for i in range(len(cost)//2):
            if cost[i] == smalest_number:
                tot += smalest_number
            elif cost[i] < (smalest_number *2 ):
                tot += cost[i]
            else:
                tot += smalest_number *2

        return tot
                