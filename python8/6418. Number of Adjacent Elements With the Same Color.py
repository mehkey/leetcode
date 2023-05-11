class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        res = []

        arr = [0] * n

        hm = defaultdict(set)

        count = 0

        for q in queries:
            
            if q[0] > 0 and arr[q[0]] !=0 and arr[q[0]-1] == arr[q[0]]:
                count -= 1
            
            if q[0] < n -1 and arr[q[0]] !=0 and arr[q[0]+1] ==  arr[q[0]]:
                count -= 1

            arr[q[0]] = q[1]

            if q[0] > 0 and arr[q[0]-1] == q[1]:
                count += 1

            if q[0] < n -1 and arr[q[0]+1] == q[1]:
                count += 1

            res.append(count)

        return res
        
        