def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

primes = set(sieve_for_primes_to(10**7))

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        M = len(mat)
        N = len(mat[0])
        
        dirs = ((1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1), (1,1) )
        
        res = 0
        
        vals = defaultdict(int)

        for i in range(M):
            for j in range(N):
                
                
                
                for dx, dy in dirs:
                    
                    cur = []
                    cur.append(str(mat[i][j]))

                    nx = i + dx
                    ny = j + dy
                    
                    while nx >= 0 and ny >= 0 and nx < M and ny < N:
                        cur.append(str(mat[nx][ny]))

                        val = int( ''.join(cur))
                        
                        if val > 10 and val in primes:
                            #res = max(res , val)
                            vals[val] += 1

                        nx += dx
                        ny += dy
                        

        if len(vals) == 0:
            return -1

        m = max(vals.values())
        ml = []
        mk = 0

        for k in vals:
            if vals[k] == m:
                mk = max(mk , k )
        
        return mk