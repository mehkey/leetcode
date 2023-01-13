/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
	res := make([]int, 0)

	res = dfs(root, res)
	return res
}

func dfs(node *TreeNode, res []int) []int {
	if node == nil {
		return res
	}
	res = append(res, node.Val)
	res = dfs(node.Left, res)
	res = dfs(node.Right, res)
	return res
}