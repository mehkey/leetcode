func minFallingPathSum(matrix [][]int) int {
	for i := 1; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {

			if j == 0 {
				matrix[i][j] += min(matrix[i-1][j+1], matrix[i-1][j])
			} else if j+1 == len(matrix[0]) {
				matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
			} else {
				matrix[i][j] += min(min(matrix[i-1][j-1], matrix[i-1][j]), matrix[i-1][j+1])
			}
		}
	}

	var m int = math.MaxInt32

	for _, val := range matrix[len(matrix)-1] {
		m = min(m, val)
	}
	return m

}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}