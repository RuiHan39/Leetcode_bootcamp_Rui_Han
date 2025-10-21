# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left, right = left.next, right.next
        return True

        
