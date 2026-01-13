class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

# inorder traversal
def in_order_traversal(root: Node) -> None:
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)
        
# DFS
def preorder(root):
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# BFS
from collections import deque
def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# better syntax:
Handling the None Case, However, since the function can also return None (if the target is not found), the return type should actually be Optional[TreeNode]. You need to import Optional from the typing module:

from typing import Optional

def dfs(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
