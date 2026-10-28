# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            current_level = []
            for _ in range(len(queue)):
                item = queue.popleft()
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                current_level.append(item.val)
            result.append(current_level)
        return result