from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    
        min_heap = []
    
    for i, l in enumerate(lists):
        if l:
            heappush(min_heap, (l.val, i, l))  # Push value, index, and node

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, i, node = heappop(min_heap)  # Extract smallest node
        current.next = node
        current = current.next
        
        if node.next:
            heappush(min_heap, (node.next.val, i, node.next))  # Push next node

    return dummy.next

# Helper function to convert a list into a linked list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example Test Cases
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]


merged_list = mergeKLists(lists)
print_linked_list(merged_list)  

# Edge Case: Empty list
print_linked_list(mergeKLists([]))  

# Edge Case: List with an empty sublist
print_linked_list(mergeKLists([[]]))  