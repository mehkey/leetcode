/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

 const maxAncestorDiff = (root: TreeNode | null): number => {

    const dfs = (node:TreeNode,min_node_value:number, max_node_value:number) : number => {

        if (!node) {
            return Math.abs(min_node_value-max_node_value);
        }
        min_node_value = Math.min(min_node_value, node.val)
        max_node_value = Math.max(max_node_value, node.val)

        return Math.max(dfs(node.left,min_node_value,max_node_value),
        dfs(node.right,min_node_value,max_node_value))

    }
    return dfs(root,root.val,root.val);
};