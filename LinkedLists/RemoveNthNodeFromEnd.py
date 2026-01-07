class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = Node(0,head)
    slow = dummy
    fast = dummy

    for i in range(n+1):
        if fast is None:
            return head
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
 
    slow.next = slow.next.next

    return dummy.next

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    n = int(input())
    res = remove_nth_from_end(head, n)
    print(" ".join(format_list(res)))
