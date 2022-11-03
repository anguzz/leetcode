# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while True:
            if fast and fast.next:           
                slow = slow.next
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
#we use two pointers to check if the list is cyclical, if the fast pointer catches up to the slow pointer then our list is a cycle 
