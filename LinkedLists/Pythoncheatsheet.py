class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterate
node = head
while node:
    print(node.val)
    node = node.next
