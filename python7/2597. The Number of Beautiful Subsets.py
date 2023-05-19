class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        '''
        nums.sort()
        
        #print(nums)

        res = []
        
        r = [0]
        
        def dfs(cur,i):

            if i == len(nums) - 1:
                r[0] += 1
                print(cur)
                return cur
            
            res = [[]]
            for j in range(i,len(nums)):

                for c in cur:
                    if c:
                        res.append(c.append(nums[j]))
                    else:
                        res.append([nums[j]])
            cur.extend(res)
            dfs(cur, i+1)
            
            return cur

        dfs([],0)
        
        return r[0]
        '''
        
        nums.sort()
        
        def powerset(seq):

            if len(seq) <= 1:
                yield seq
                yield []
            else:
                for item in powerset(seq[1:]):
                    if item and all(item[i] - seq[0] != k for i in range(len(item))):
                        yield [seq[0]]+item
                    if not item:
                        yield [seq[0]]
                    yield item
        
        r = [x for x in powerset(nums)]
        
        #print(r)
        return len(r)-1
        