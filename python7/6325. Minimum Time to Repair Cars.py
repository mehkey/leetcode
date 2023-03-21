class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        ranks.sort()

        l = 0
        r = max(ranks) * cars * cars 

        res = float('inf')

        def test(m):

            count = 0

            for r in ranks:
                count += floor( sqrt( m / r ) )

                if count >= cars:
                    return True

            return False

        while l <= r:

            m = (l+r)//2

            if test(m):
                res = min(res,m)
                r = m -1
            else:
                l = m+1

        return res
    

     def repairCars(self, A: List[int], cars: int) -> int:
        count = Counter(A)
        h = [[a, a, 1, count[a]] for a in count]
        heapify(h)
        while cars > 0:
            time, rank, k, count = heappop(h)
            cars -= count
            k += 1
            heappush(h, [rank * k * k, rank, k, count])
        return time