class Solution:
    def isPossible(self, A):

        lens = collections.defaultdict(list)

        for n in A:

            if lens[n-1]:
                cur = heappop(lens[n-1])
                heappush(lens[n], cur+1 )

            else:
                heappush(lens[n], 1)

        #print(lens)
        for len_arr in lens.values(): 
            if len_arr and min(len_arr) < 3:
                return False           
        
        return True
    
        """
        lens = collections.defaultdict(list)
        for n in A:
            print(lens)
            length = 1
            print(n)
            print(len(lens[n - 1]))
            if len(lens[n - 1]) > 0:
                length += heapq.heappop(lens[n - 1])
            heapq.heappush(lens[n], length)
        print(lens)
        for len_arr in lens.values():
            if len_arr and min(len_arr) < 3: return False           
        return True
        """
    
        