# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: #recursive approach
        if not head:  #base case
            return None
        
        
        new = head 
        if head.next:
            new = self.reverseList(head.next)
            head.next.next = head #reverse link between next and head
        head.next = None    
        return new
        
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:   #iterative approach
        prev=None
        curr=head    
        while curr:          #not null
            temp = curr.next
            curr.next= prev  
            prev = curr
            curr = temp
        return prev
            
