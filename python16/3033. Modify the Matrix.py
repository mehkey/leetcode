class Solution:
    def modifiedMatrix(self, m: List[List[int]]) -> List[List[int]]:
        M = len(m)
        N = len(m[0])
        ans = [[0]*N for _ in range(M)]
        
        cm = defaultdict(int)
        for i in range(M):
            for j in range(N):
                ans[i][j] = m[i][j]

                cm[j] = max(cm[j],m[i][j])
        
        for i in range(M):
            for j in range(N):
                if ans[i][j] == -1:
                    ans[i][j] = cm[j]
        
        return ans
