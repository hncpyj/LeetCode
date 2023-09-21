# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        cnt = 0
        reverse = None

        while fast and fast.next:
            fast = fast.next.next
            if fast is not None and fast.next is None:
                cnt+=1
            nxt = slow.next
            slow.next = reverse
            reverse = slow
            slow = nxt
            cnt += 1
        
        if fast:
            slow = slow.next
        while reverse and slow:
            if reverse.val != slow.val:
                return False
            reverse = reverse.next
            slow = slow.next

        return True
            


            
        