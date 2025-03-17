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
