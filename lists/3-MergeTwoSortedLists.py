#Definition for singly-linked list.
#class ListNode:
#def __init__(self, val=0, next=None):
#self.val = val
#self.next = next
class Solution:
    def mergeTwoLists(self, lis1: ListNode, lis2: ListNode) -> ListNode:
        #using array to merge the list 
        arr1 = []
        while (lis1):
            arr1.append(lis1.val)
            lis1 = lis1.next    
			
        arr2 = []
        while (lis2):
            arr2.append(lis2.val)
            lis2 = lis2.next
			
        arr3 = arr1+arr2
        arr3 = sorted(arr3)
        
        ans = ansList = ListNode(-1)
        
        for i in arr3:
            ans.next = ListNode(i)
            ans = ans.next
        
        return ansList.next
