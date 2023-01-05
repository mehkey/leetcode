class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        #c = Counter(text)
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        #return max(c.values())
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in xrange(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res



        dict1, ans, max_len = defaultdict(int), [], 0

        for i in text:
            dict1[i] += 1

            if ans and ans[-1][0] == i:
                ans[-1][1] += 1
            else:
                ans.append([i,1])

        for i, j in ans:
            max_len = max(max_len, min(j+1, dict1[i]))

        for i in range(1, len(ans)-1):
            if ans[i-1][0] == ans[i+1][0] and ans[i][1] == 1:
                max_len = max(max_len, min(ans[i-1][1] + ans[i+1][1] + 1, dict1[ans[i+1][0]]))

        return max_len
