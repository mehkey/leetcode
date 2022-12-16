func longestCommonSubsequence(text1 string, text2 string) int {

	m := len(text1)
	n := len(text2)
	if m == 0 || n == 0 {
		return 0
	}
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {

			if text1[i] == text2[j] {
				if i > 0 && j > 0 {
					dp[i][j] = dp[i-1][j-1] + 1
				} else {
					dp[i][j] = 1
				}
			} else {
				if i > 0 && j > 0 {
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
				} else if i > 0 {
					dp[i][j] = dp[i-1][j]
				} else if j > 0 {
					dp[i][j] = dp[i][j-1]
				}
			}
		}
	}
	fmt.Println(dp)
	return dp[m-1][n-1]
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}