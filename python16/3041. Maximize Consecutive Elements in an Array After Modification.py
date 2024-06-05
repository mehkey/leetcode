
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        

        c = Counter(nums)
        

        @cache
        def dfs(cur, minus):

            res = 0

            # try to skip 2 
            if c[cur] - minus >= 1  :

                # check if 2 away has enough count
                if cur + 2 in c: 
                    res = max( res, dfs(cur+2,1) + 2)

                # check if we can increment the next to jump 2
                if cur + 1 in c:
                    res = max( res, dfs(cur+2,0) + 2)

            # try to skip 1 using if the next has enohg count
            if cur + 1 in c:
                res = max( res, dfs(cur+1,1) + 1)

            # try to skip 1 using the current value incremented
            if c[cur] - minus >= 1  :
                res = max( res, dfs(cur+1,0) + 1)

            return res
        
        res = 0
        for n in nums:

            res = max( res, dfs(n, 1) + 1 )

            res = max( res, dfs(n+1,0) + 1 )

        return res

A.sort()
        pre = -10
        res = c1 = c2 = 1
        for a in A:
            if a == pre:
                c2 = c1 + 1
            elif a == pre + 1:
                c1, c2 = c1 + 1, c2 + 1
            elif a == pre + 2:
                c1, c2 = c2 + 1, 1
            else:
                c1 = c2 = 1
            res = max(res, c1, c2)
            pre = a
        return res


def maxSelectedElements(self, A: List[int]) -> int:
        dp = defaultdict(int)
        A.sort()
        for a in A:
            dp[a + 1] = dp[a] + 1
            dp[a] = dp[a - 1] + 1
        return max(dp.values())


class Solution {
public:
    int maxSelectedElements(vector<int>& A) {
        unordered_map<int, int> dp;
        sort(A.begin(), A.end());
        int res = 0;
        for (int& a : A) {
            res = max(res, dp[a + 1] = dp[a] + 1);
            res = max(res, dp[a] = dp[a - 1] + 1);
        }
        return res;
    }
};


3041. Maximize Consecutive Elements in an Array After Modification