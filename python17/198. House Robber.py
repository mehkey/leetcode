

func rob(nums []int) int {
    prev := 0
    prev_prev := 0

    for _,v := range nums {
        cur := max(prev_prev + v,prev)
        prev_prev = prev
        prev = cur

    }

    return prev
}

func max(a int, b int) int{
    if a >= b{
        return a
    }
    return b
}