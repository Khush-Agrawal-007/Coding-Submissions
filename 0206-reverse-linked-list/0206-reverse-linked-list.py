class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Temporarily store the next node so we don't lose the list
            next_node = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Shift 'prev' and 'curr' one step forward
            prev = curr
            curr = next_node

        # After the loop, curr is None and prev is the new head
        return prev
