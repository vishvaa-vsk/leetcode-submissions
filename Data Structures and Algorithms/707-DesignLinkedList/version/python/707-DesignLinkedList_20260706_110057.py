# Last updated: 06/07/2026, 11:00:57
1class ListNode:
2    def __init__(self,val):
3        self.val = val
4        self.next = None
5
6class MyLinkedList:
7
8    def __init__(self):
9        self.head = None
10        self.size = 0
11        
12
13    def get(self, index: int) -> int:
14        if index < 0 or index >= self.size:
15            return -1
16        
17        current = self.head
18
19        for _ in range(0,index):
20            current = current.next
21        
22        return current.val
23
24
25    def addAtHead(self, val: int) -> None:
26        self.addAtIndex(0,val)
27        
28
29    def addAtTail(self, val: int) -> None:
30        self.addAtIndex(self.size,val)
31        
32
33    def addAtIndex(self, index: int, val: int) -> None:
34        if index > self.size:
35            return
36        
37        current = self.head
38        new_node = ListNode(val)
39
40        if index <= 0:
41            new_node.next = current
42            self.head = new_node
43        else:
44            for _ in range(index - 1):
45                current = current.next
46            new_node.next = current.next
47            current.next = new_node
48        
49        self.size += 1
50
51    def deleteAtIndex(self, index: int) -> None:
52        if index < 0 or index >= self.size:
53            return
54        
55        current = self.head
56
57        if index == 0:
58            self.head = self.head.next
59        else:
60            for _ in range(index - 1):
61                current = current.next
62            current.next = current.next.next
63        
64        self.size -= 1
65        
66
67
68# Your MyLinkedList object will be instantiated and called as such:
69# obj = MyLinkedList()
70# param_1 = obj.get(index)
71# obj.addAtHead(val)
72# obj.addAtTail(val)
73# obj.addAtIndex(index,val)
74# obj.deleteAtIndex(index)