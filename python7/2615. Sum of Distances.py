class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        N = len(nums)

        res = [0] * N

        #hm = defaultdict(int)
        hm = defaultdict(list)
        hm2 = defaultdict(int)
        hm3 = defaultdict(list)
        resCount = defaultdict(int)
        resSum = defaultdict(int)
        
        # sorted list -> binary search on that list
        for i in range(N):
            
            '''for j in hm[nums[i]]:

                res[i] += abs(i-j)
                
                res[j] += abs(j-i)
            '''
            res[i] += resCount[nums[i]] - i *resSum[nums[i]]  #abs(i-j)
                
            #res[j] -= resCount[nums[i]] + i *resSum[nums[i]] #resCount[nums[i]]#abs(j-i)
            #hm[nums[i]].append(i)
            #hm3[nums[i]].append(hm2[nums[i]] + i)
            #hm2[nums[i]] += i
            resCount[nums[i]] += i
            resSum[nums[i]] += 1
        
        #print(hm)
        #print(hm2)
        #print(hm3)

        return res

        