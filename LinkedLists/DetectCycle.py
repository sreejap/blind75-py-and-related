class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:    
    slow = nodes
    fast = nodes

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
