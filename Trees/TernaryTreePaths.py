class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


    def ternary_tree_paths(root: Node) -> list[str]:
        res = []
        def dfs (node,path,res):
            if not node:
                return
            if all (c is None for c in node.children):
                res.append('->'.join(path+[str(node.val)]))
    
            for child in node.children:
                if child is not None:                 
                    path.append (str(node.val))
                    
                    dfs (child,path,res)
                    path.pop() # this removes from the path
    
        if root:
            dfs (root,[],res)
        return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
