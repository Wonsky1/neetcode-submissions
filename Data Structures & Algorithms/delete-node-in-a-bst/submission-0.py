# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find a node
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            # 0-1 edges
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 2 edges
            node = root.right

            while node.left:
                node = node.left
            # print(node.val)
            root.val = node.val
            root.right = self.deleteNode(root.right, node.val)
            

        # node = root
        # while node != key:
        #     if node.val > key:
        #         node = node.left
        #     if node.val < key:
        #         node = node.right
        #     else:
        #         break
        # # if 0-1 edges:
        # if not node.right or not node.left:
        #     if node.right:
        #         node.val = node.right.val
        #     if node.left:
        #         node.val = node.right.val
        #     node.right = node.left = None
        #     return root
        
        # # if 2 edges:
        # biggest_node_to_left = node.left
        # while biggest_node_to_left.right:
        #     biggest_node_to_left = node.right
        
        # node = self.deleteNode(node.left, biggest_node_to_left.val)
        
        
        return root