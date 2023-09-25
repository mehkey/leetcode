class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:

        #hx = defaultdict(int)
        #hy = defaultdict(int)
        hm = defaultdict(int)

        t = 0
        res = 0

        for x,y in coordinates:

            for i in range(0,k+1):
                j = k - i

                res += hm[(x^i,y^j)]

            hm[(x,y)] += 1

        return res

        '''
        #print(x^y )
        #bin(n).count("1")

        if ( bin(x^y).count("1") +k or bin(x^y).count("1") -k  ) in hc:
            t += hc[bin(x^y).count("1")]

        #bin(n).count("1")
        print(bin(x^y).count("1"))
        hc[bin(x^y).count("1")] += 1
        #return False
        #if x^y in hc:
        #    t += hc[x^y]

        #if x in hx[x] and y in hy[y] :

        #number of different bits += 1

        #number of different bits -= 1

        #hx[x] += 1
        #hy[y] += 1

        #hc[x^y]

        print(hc)
        '''
        return t
