class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    def check_height (tree:Node) -> tuple[bool, int]:
        if not tree:
            return True,-1
        left_ok, left_h = check_height(tree.left)
        right_ok, right_h = check_height(tree.right)
        balanced = left_ok and right_ok and abs(left_h - right_h) <=1 #make sure every code path returns a value
        return balanced, max(left_h,right_h)+1
    is_balanced_tree, total_h = check_height(tree)        
    return is_balanced_tree
