class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        if(len(nums) == 1):
            return [nums.copy()]
        
        for i in range(len(nums)):
            val = nums.pop(0) # pop 3   
            
            temp = self.permute(nums) # array [1,2]  [2,1]  etc [1,2,3]  [2,1,3]  
            
            for j in temp:
                j.append(val)
            
            res.extend(temp)
            
            nums.append(val)
        
        return res



        """
        




        
        """

        class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #nums=[1,2,3]
        n=len(nums)

        dp=[[[x] for x in nums]]

        for i in range(1,n):
            dp.append([])
            for j in nums:
                for k in range(len(dp[i-1])):
                    #print(f'i={i},j={j},k={k},len dp = {len(dp)}')
                    if(j not in dp[i-1][k]):
                        dp[i].append(dp[i-1][k]+[j])

        return dp[n-1]    


    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            dp = [[nums[0]]]
            for i in range(1,len(nums)):
                res = []
                #print(dp)
                for combo in dp:
                    for j in range(i + 1):
                        res += [combo[:j] + [nums[i]] + combo[j:]] # insert nums[i] at idx 0 : len(current combo) each time to generate combinations from length = len(current combo)  -->  len(current comb0) + 1
                        #print(res)
                dp = res
            return dp

    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        queue = collections.deque()
        queue.append([])
        
        for el in nums:
            
            level = len(queue)
            
            for i in range(level):
                
                popped = queue.popleft()
                
                for num in nums:
                    if num not in popped:
                        new_element = popped + [num]
                        queue.append(new_element)
                        
        return queue


    



        def permute(self, nums):
            stack = [(nums,[])]
            res = []
            while stack :
                numb,ls = stack.pop()
                if numb:
                    for i in range(0,len(numb)):
                        tmp = [] + numb
                        tmp2 = tmp.pop(i)
                        stack.append((tmp,ls+[tmp2]))
                else:
                    res.append(ls)
            return res


#backtrack
    class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visited = [], []
        def dfs(row):
            if len(row) == len(nums):
                res.append(row[:])
                row = []
                return 
            
            for num in nums:
                if num in visited:
                    continue
                visited.append(num)
                row.append(num)
                
                dfs(row)
                # backtrack both visited and row 
                visited.pop()
                row.pop()
                
        dfs([])
        return res




        q = deque()
        q.append((nums,[]))
        
        res = []
        
        while q :
            
            numb,ls = q.popleft()
            #print("numb",numb)
            print("ls",ls)
            if numb:
                for i in range(0,len(numb)):
                    tmp = [] + numb
                    tmp2 = tmp.pop(i)
                    q.append((tmp,ls+[tmp2]))
            else:
                res.append(ls)
        return res



        