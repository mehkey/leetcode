/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxAncestorDiff(root *TreeNode) int {
	return dfs(root, root.Val, root.Val)
}

func dfs(node *TreeNode, min_node_value int, max_node_value int) int {

	if node == nil {
		return int(math.Abs(float64(min_node_value - max_node_value)))
	}

	min_node_value = min(min_node_value, node.Val)
	max_node_value = max(max_node_value, node.Val)

	return max(dfs(node.Left, min_node_value, max_node_value),
		dfs(node.Right, min_node_value, max_node_value))

}

func max(i, j int) int {
	if i < j {
		return j
	}
	return i
}

func min(i, j int) int {
	if i > j {
		return j
	}
	return i
}
