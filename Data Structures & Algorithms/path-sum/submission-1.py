# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum: int = 0) -> bool:
        if not root:
            return False
        currentSum += root.val
        if not root.right and not root.left:
            return targetSum == currentSum
        if root.left and self.hasPathSum(root.left, targetSum, currentSum):
            return True
        if root.right and self.hasPathSum(root.right, targetSum, currentSum):
            return True
        return False