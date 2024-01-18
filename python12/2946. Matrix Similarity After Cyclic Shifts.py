class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        M = len(mat)
        N = len(mat[0])

        #print((13) % 10 )

        for i in range(M):
            if i % 2 == 0:
                for j in range(N-1,-1,-1):
                    if mat[i][j] != mat[i][(j+k)%N]:
                        return False
            else:
                for j in range(N-1,-1,-1):
                    if mat[i][j] != mat[i][(j-(k%N))]:
                        return False

        return True 