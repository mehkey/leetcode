class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:

        M = len(image)
        N = len(image[0])
        
        mask = [[1]*N for j in range(M)]

        avg = [[inf]*N for j in range(M)]
        
        res = [[inf]*N for j in range(M)]

        dd = (0,0), (0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)

        for i in range(1,M-1):
            for j in range(1,N-1):
                
                '''
                for a in range(i-1,i+2):
                    for b in range(j-1, j+2):

                        if b == j- 1 or b == j and abs(image[a][b] - image[a+1][b]) > threshold :
                            mask[i][j] = 0
                            break
                        if a == i-1 or a == i and abs(image[a][b] - image[a][b+1]) > threshold:
                            mask[i][j] = 0
                            break
                        
                    if mask[i][j] == 0:
                        break
                '''
                
        for i in range(1,M-1):

            for j in range(1,N-1):
                
                if mask[i][j] == 0:
                    continue

                tot = 0

                for dx, dy in dd:
                    tot += image[i + dx][j + dy]
                

                avg[i][j] = floor(tot / 9)
        

        for i in range(M):

            for j in range(N):
                if mask[i][j] == 0:
                    res[i][j] = image[i][j]
                    continue
                    
                tot = 0
                count = 0

                for dx, dy in dd:
                    if 0 <= i+dx < M and 0 <= j + dy < N and avg[i+dx][j+dy] != inf:
                        tot += avg[i+dx][j+dy] 
                        count += 1
                
                if count == 0:
                    res[i][j] = image[i][j]
                else:
                    res[i][j] = floor(tot / count)
        
        return res
                
                