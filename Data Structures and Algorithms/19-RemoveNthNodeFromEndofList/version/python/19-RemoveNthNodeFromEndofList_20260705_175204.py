# Last updated: 05/07/2026, 17:52:04
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10
11        slow = dummy
12        fast = dummy
13
14        for _ in range(n+1):
15            fast = fast.next
16        
17        while fast:
18            fast = fast.next
19            slow = slow.next
20
21        slow.next = slow.next.next
22    
23        return dummy.next
24        
25        