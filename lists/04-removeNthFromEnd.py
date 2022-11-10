
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head) #insert dummy at start
        left = dummy           #point left to dummy
        right=head             #point right to head 
        
        while(n>0 and right):   #shift right until we hit n
            right=right.next
            n-=1                #decrement n to keep track of shifts
        
        #at this point pointers are set up so now just loop increment and delete
        
        
        while right:            #shift left and right until end of list
            left=left.next
            right=right.next
            
        left.next = left.next.next #repoint to end of list
        
        return dummy.next
        
        
''' visualized
[1,2,3,4,5], n = 2
two pointer approach 

insert dummy pointer at head of list and point left to it
point right pointer n+1 of left (in this case 2+1 due to offset from dummy)


loop through with both pointers 
D 1 2 3 4 5 
L     R

D 1 2 3 4 5 
  L     R

D 1 2 3 4 5 
    L     R
    
D 1 2 3 4 5 NULL
      L     R
      
when the right pointer hits NULL, signifies end of list
so now update left pointer to point at R-1 (3-->5) to delete 4
return dummy which was at head of list to return updated list 
'''
        
