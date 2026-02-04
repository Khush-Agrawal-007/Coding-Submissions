# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two dummy heads
        small_head = ListNode(0)
        large_head = ListNode(0)
        
        # Pointers to the current end of each list
        small = small_head
        large = large_head
        
        current = head
        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next
            current = current.next
        
        # Important: Terminate the large list to prevent cycles
        large.next = None
        
        # Connect the small list to the large list
        # small_head.next is the first real node of the small list
        # large_head.next is the first real node of the large list
        small.next = large_head.next
        
        return small_head.next