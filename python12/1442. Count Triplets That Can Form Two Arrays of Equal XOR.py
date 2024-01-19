class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        count = 0
        n = len(arr)
        pre = [0]* (n+1)

        for i in range(1,n+1):
            pre[i] = pre[i-1] ^ arr[i-1]

        print(pre)
        
        '''
        [2,3,1,6,7]

        10
        11
        01
       110
       111

         0,10, 01, 0, 110, 001 

        '''

        res = 0

        for i in range(0,n+1):

            for j in range(i+1,n+1):

                if pre[i] == pre[j]:
                    res += j - i - 1
        
        return res

        for j in range(1,n):


            a = 0

            for i in range(j-1,-1,-1):
                a ^= arr[i]

                b = 0
                for k in range(j,n):
                    b ^= arr[k]
                    
                    if a == b:
                        count += 1
        
        return count
            

def countTriplets(self, A):
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res
        
        