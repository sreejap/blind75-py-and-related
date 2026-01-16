class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_same_Tree(tree1:Node, tree2:Node) -> bool:
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (tree1.val == tree2.val and (is_same_Tree(tree1.left, tree2.left)) and (is_same_Tree(tree1.right, tree2.right)))

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    if not root:
        return False
    return is_same_Tree (root,sub_root) or is_same_Tree (root.left, sub_root) or is_same_Tree (root.right, sub_root)
