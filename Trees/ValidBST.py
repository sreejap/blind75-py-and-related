from math import inf
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def dfs (root, min_val, max_val):        
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return dfs (root.left,min_val,root.val) and dfs (root.right,root.val, max_val)

    return dfs(root, -inf, inf)
