# Last updated: 05/07/2026, 21:57:58
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
9        lista = headA
10        listb = headB
11
12        while lista != listb:
13            lista = lista.next if lista else headB
14            listb = listb.next if listb else headA
15        
16        return listb