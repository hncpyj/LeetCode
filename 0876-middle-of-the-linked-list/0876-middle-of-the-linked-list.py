# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = None
        cnt = 0
        origin = head
        while head:
            head = head.next
            cnt += 1
        head = origin
        harf = int(cnt/2)
        for i in range(harf):
            head = head.next
        return head