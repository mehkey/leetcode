class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        odd = [] #[0] * len(nums) // 2 + 1
        even = [] #[0] * len(nums) // 2 + 1

        j = 0
        for i,v in enumerate(nums):
            odd[j].append(i)
            
            

        return res
    
    def sortEvenOdd(self, A):
        A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
        return A
    
    
    if len(nums) == 2:
            return nums
        else:
            evensorted = []
            oddsorted = []
            for i in range(len(nums)):
                if i%2 == 0:
                    evensorted.append(nums[i])
                else:
                    oddsorted.append(nums[i])
            evensorted.sort()
            oddsorted.sort(reverse=True)
            
            evenindex = 0
            oddindex = 0
            for i in range(len(nums)):
                if i%2==0:
                    nums[i] = evensorted[evenindex]
                    evenindex += 1
                else:
                    nums[i] = oddsorted[oddindex]
                    oddindex += 1
        return nums