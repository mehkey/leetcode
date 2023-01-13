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

 function preorderTraversal(root: TreeNode | null): number[] {
    const output = new Array();
    dfs(root, output);
    return output
};

const dfs = (node: TreeNode, output: number[]) => {
    if (node === null){
        return ;
    }

    output.push(node.val)
    dfs(node.left,output);
    dfs(node.right,output);

};