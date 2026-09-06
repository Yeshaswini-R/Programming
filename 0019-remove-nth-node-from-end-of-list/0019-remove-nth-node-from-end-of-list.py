# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        save = head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.pop(len(arr) - n)
        if not arr:
            return None
        head = save
        for i, val in enumerate(arr):
            head.val = val
            if i == len(arr) - 1:
                head.next = None
            else:
                head = head.next
        return save