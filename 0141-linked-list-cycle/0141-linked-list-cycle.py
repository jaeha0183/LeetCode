# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force: hash set of visited nodes
        #   -> O(n) time, O(1) space
        
        # edge cases:
        # - head is None
        # - single node, no cycle / self - loop
        # - cycle back to head (pos = 0)

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False