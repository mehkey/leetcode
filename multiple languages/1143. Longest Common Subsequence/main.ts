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