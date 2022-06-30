class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        """
        
        Find all the duos ( subset of size 2 and calculate the maximum)
        
        Return the maximum
        
        2^n * n
        
        
        Last 2 numbers ( fruits )
        What are the last 2 fruits?
        
        keep moving right and add more fruits
        
        Unitl a new tree, then save the total to max
        
        
        
        2 Fruit
        last fruit is A... remember how many times A repeated
        last fruit is B... remember how many times B repeated
        
        
        runtime: O(n)   space: O(1)
        
        
        """
        
        repeated = 0
        
        count = 0
        
        current = 0
        
        previous = 0
        
        last = 0
        
        l = len(fruits)
        
        if l == 1:
            return 1
        if l == 2:
            return 2
        
        #current = fruits[1]
        #previous = fruits[0] if fruits[1] != fruits[0] else 0
        #repeated = 0 if fruits[1] != fruits[0] else 1
        
        m = 0
        
        for i in range(0,l):
            #print(i, current, previous, count, repeated)
            if fruits[i] == current:
                repeated += 1
                count += 1
            elif fruits[i] == previous:
                repeated = 1
                count += 1
                current, previous = previous, current
            else:
                previous = current
                current = fruits[i]
                
                count = repeated + 1 
                
                repeated = 1

            m = max(m, count )
            
        print(i, current, previous, count, repeated)
        
        return m
        
        
        def totalFruit(self, tree):
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1 
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res
        
        