# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # follows the pattern of inorder traversal
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # traverse the tree and make a list
        # then get the list and get the next el 
        # self.res: List[TreeNode] = []
        self.found = False
        self.successor = None

        def helper (node, p):
            if not node or self.successor:
                return     

            helper (node.left, p)

            if self.found and not self.successor:
                self.successor = node
                return
            
            if node.val == p.val:
                self.found = True

            helper (node.right, p)           


        helper (root,p)
        return self.successor

        
