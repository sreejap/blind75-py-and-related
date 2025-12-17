# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        level = 0
        if not root:
            return levels

        queue = deque ([root])

        while queue:
            qSize = len(queue)
            levels.append ([]) # adding empty list
            for i in range (qSize):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            level += 1
        
        return levels
