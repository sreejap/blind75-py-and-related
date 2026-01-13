class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    def dfs(root:Node) -> int:
        if not root:
            return 0
        return max (dfs(root.left), dfs(root.right)) + 1     # we count the number of nodes in the dfs method
    return dfs (root) - 1 if root else 0 # we subtract 1 because we want the edges in the answer as defined in the problem https://algo.monster/problems/tree_max_depth
