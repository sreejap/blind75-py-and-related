class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delete(tree, val):
    if tree is None:
        return None
    if val < tree.val:
        tree.left = delete(tree.left, val)
    elif val > tree.val:
        tree.right = delete(tree.right, val)
    else:
        # Node to delete found
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        # Node with two children: get the inorder successor (smallest in the right subtree)
        successor = tree.right
        while successor.left:
            successor = successor.left
        tree.val = successor.val
        tree.right = delete(tree.right, successor.val)
    return tree
