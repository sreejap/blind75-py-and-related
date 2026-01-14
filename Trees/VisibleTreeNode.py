from math import inf
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs (root:Node, max_val:int):
        if not root:
            return 0
        total = 0
        if root.val >= max_val:            
            total +=1
        
        total += dfs(root.left, root.val)
        total += dfs(root.right, root.val)        
        return total
    
    return dfs(root, -inf)  
