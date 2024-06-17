
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int maxAncestorDiff(TreeNode root) {
        return dfs(root, root.val, root.val);
    }

    public int dfs(TreeNode node, int min_node_value, int max_node_value) {
        if (node == null) {
            return Math.abs(min_node_value - max_node_value);
        }
        min_node_value = Math.min(min_node_value, node.val);
        max_node_value = Math.max(max_node_value, node.val);

        return Math.max(dfs(node.left, min_node_value, max_node_value),
                dfs(node.right, min_node_value, max_node_value));
    }
}