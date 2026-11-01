# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height_of_bs_tree(self, root) -> int:
        if not root:
            return 0
        left_sum = self.height_of_bs_tree(root.left)
        right_sum = self.height_of_bs_tree(root.right)
        return 1 + max(left_sum, right_sum)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root or not root.right or not root_left:
        if not root: 
            return 0
        times_went_down = 0
        while not root.left or not root.right:
            if root.left:
                times_went_down += 1
                root = root.left
            elif root.right:
                times_went_down += 1
                root = root.right
            else:
                break
            
        return max(self.height_of_bs_tree(root.left) + self.height_of_bs_tree(root.right), times_went_down)
