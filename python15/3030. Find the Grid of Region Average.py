class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:

        M = len(image)
        N = len(image[0])
        
        mask = [[1 for _ in range(N)] for j in range(M)]

        avg = [[inf for _ in range(N)] for j in range(M)]
        
        res = [[inf for _ in range(N)] for j in range(M)]

        dd = (0,0), (0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)

        for x in range(1,M-1):
            for y in range(1,N-1):

                for a in range(x-1,x+2):
                    for b in range(y-1,y+2):
                        if a + 1 < x+2 and abs(image[a][b] - image[a+1][b]) > threshold:
                            mask[x][y] = 0
                            continue
                        if b+1 < y+2 and abs(image[a][b] - image[a][b+1]) > threshold:
                            mask[x][y] = 0
                            continue
                    if mask[x][y] == 0:
                        continue

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