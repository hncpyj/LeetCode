# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        front = head
        back = head.next

        while front != back:
            if not back:
                return False
            elif not back.next:
                return False

            front = front.next
            back = back.next.next
    
        return True
