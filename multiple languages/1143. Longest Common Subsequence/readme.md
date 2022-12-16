```go
func longestCommonSubsequence(text1 string, text2 string) int {
    
    m := len(text1)
    n := len(text2)
    if(m == 0 || n == 0) {
        return 0
    }
    dp := make([][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++  {

            if text1[i] == text2[j]  {
                if i > 0 && j > 0 {
                    dp[i][j] = dp[i - 1][j - 1] + 1
                } else {    
                    dp[i][j] = 1
                }
            } else {
                if  i > 0 && j > 0 {
                    dp[i][j] = max(dp[i - 1][j],dp[i][j-1])
                } else if i > 0 {
                    dp[i][j] = dp[i - 1][j]
                } else if j > 0 {
                    dp[i][j] = dp[i][j-1]
                }
            }
        }
    }
    fmt.Println(dp)
    return dp[m - 1][n - 1];
}

func max(a int, b int) int {
    if a >= b{
        return a
    }
    return b
}
```


```c++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(), n = text2.size();
        if(m == 0 || n == 0) 
            return 0;

        vector<vector<int>> dp(m , vector<int> (n, 0));

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(text1[i] == text2[j]) {
                    dp[i][j] = (i > 0 && j > 0? dp[i - 1][j - 1]: 0) + 1;
                }else {
                    dp[i][j] = max((i > 0? dp[i - 1][j]: 0), (j > 0? dp[i][j - 1]: 0));
                }
            }
        }
        return dp[m - 1][n - 1];

    }
};
```



```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {

        int m = text1.length(), n = text2.length();
        if(m == 0 || n == 0) return 0;
        int[][] dp = new int[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = (i > 0 && j > 0? dp[i - 1][j - 1]: 0) + 1;
                }else {
                    dp[i][j] = Math.max((i > 0? dp[i - 1][j]: 0), (j > 0? dp[i][j - 1]: 0));
                }
            }
        }
        return dp[m - 1][n - 1];

    }
}
```


```typescript
function longestCommonSubsequence(text1: string, text2: string): number {

    let m = text1.length, n = text2.length;
    if(m == 0 || n == 0) return 0;
    let dp : number[][] = [];
    for(let i :number = 0; i < m; i++) {
        dp[i]  = [];
        for(let j :number= 0; j < n; j++) {
            if(text1.charAt(i) == text2.charAt(j)) {
                dp[i][j] = (i > 0 && j > 0? dp[i - 1][j - 1]: 0) + 1;
            }else {
                dp[i][j] = Math.max((i > 0? dp[i - 1][j]: 0), (j > 0? dp[i][j - 1]: 0));
            }
        }
    }
    console.log(dp);
    return dp[m - 1][n - 1];
};
```