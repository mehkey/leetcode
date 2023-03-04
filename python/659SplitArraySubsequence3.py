class Solution:
    def isPossible(self, A):
        
       
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            print(left)
            print(end)
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
            
        return True
    

    class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        lens = collections.defaultdict(list)
        for n in nums:
            length = 1
            if len(lens[n - 1]) > 0:
                length += heapq.heappop(lens[n - 1])
            heapq.heappush(lens[n], length)
        for len_arr in lens.values():
            if len_arr and min(len_arr) < 3: return False           
        return True