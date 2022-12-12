func climbStairs(n int) int {

	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	var prev_prev int = 1
	var prev int = 2
	var result int = 0
	var i int = 0
	for i = 0; i < n-2; i++ {
		result = prev_prev + prev
		prev_prev = prev
		prev = result
	}
	return result

}