/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        //def dfs(node:TreeNode,min_node_value:int, max_node_value:int) -> int:

        return dfs(root,root->val,root->val);
    }

    int dfs(TreeNode* node, int min_node_value, int max_node_value){
        if (!node){
            return abs(min_node_value-max_node_value);
        }

        //if not node:
        //        return abs(min_node_value-max_node_value)
            
        min_node_value = min(min_node_value, node->val);
        max_node_value = max(max_node_value, node->val);

        return max(dfs(node->left,min_node_value,max_node_value),
                dfs(node->right,min_node_value,max_node_value));
    }
};