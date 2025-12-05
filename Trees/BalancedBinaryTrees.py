class Solution:

    def height (self,root:Optional[TreeNode]) -> int:
        if not root: # if root is none, it is falsy value, not falsy is true
            return -1
        return 1 + max (self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return (abs(self.height(root.left) - self.height (root.right)) < 2
                 and self.isBalanced (root.left)
                 and self.isBalanced (root.right)
               )
