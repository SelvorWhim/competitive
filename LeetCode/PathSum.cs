/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public bool HasPathSum(TreeNode root, int sum)
    {
        if (root == null) // make sure it doesn't return true for partial paths because of nodes with single children
        {
            return false;
        }
        if (root.left == null && root.right == null) // leaf
        {
            return (sum == root.val);
        }
        int sumRemnant = sum - root.val;
        return (HasPathSum(root.left, sumRemnant) || HasPathSum(root.right, sumRemnant));
    }
};
