class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.val = value  # Fixed: consistent naming
        self.next = next

class MyHashMap:
    def __init__(self):
        # Create 1000 dummy nodes to simplify insertion/deletion logic
        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return 
            cur = cur.next
        # If key doesn't exist, append new node at the end of the chain
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next # Start at the first actual data node
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        # Look ahead to the next node to allow for easy deletion
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next