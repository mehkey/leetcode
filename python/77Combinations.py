class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        current = []

        def dfs(start):

            if len(current) == k  :
                res.append(current.copy())
                return

            for number in range(start,n +1 ):

                current.append(number)
                dfs(number+1)
                current.pop()

        dfs(1)

        return res

                