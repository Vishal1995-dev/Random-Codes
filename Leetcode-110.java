/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean balance = true;
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        return (Math.abs(depth(root.left) - depth(root.right)) <= 1) && balance;
    }
     public int depth(TreeNode root) {
        if (balance) {
            if (root == null)
                return 0;

            int lengthOfLeft = depth(root.left);
            int lengthOfRight = depth(root.right);

            if (Math.abs(lengthOfLeft - lengthOfRight) > 1) {
                balance = false;
                return 0;
            }
            return Math.max(lengthOfLeft, lengthOfRight) + 1;
        } else {
            return 0;
        }
     }
}
