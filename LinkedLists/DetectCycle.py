class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:
    dummy = Node(0,nodes)
    slow = dummy
    fast = dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
