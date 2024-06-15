def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi


def match(s, pat):
    pi = partial(pat)

    g, idx = 0, []
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            idx.append(i + 1 - g)
            g = pi[g - 1]

    return idx

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        
        s = []
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                s.append(0)
            if nums[i] < nums[i+1]:
                s.append(1)
            if nums[i] > nums[i+1]:
                s.append(-1)
        
        res = match(s, pattern)
          
        return len(res)