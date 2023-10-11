from typing import List
from typing import Optional
import queue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = queue.PriorityQueue()
        for i in range(len(lists)):
            l = lists[i]
            while(l != None):
                q.put(l.val)
                l = l.next
        if q.empty():
            return None
        rlt = ListNode()
        rlt.val = q.get()
        rlt.next = None
    
        new_node = rlt
        while not q.empty():
            new_node.next = ListNode()
            new_node = new_node.next
            new_node.val = q.get()
            new_node.next = None
        
        return rlt
        

aaa = ListNode(0, ListNode(2, ListNode(4)))
bbb = ListNode(1, ListNode(3, ListNode(4)))
ccc = ListNode(5, ListNode(6))
ddd = ListNode(None)

tttt = Solution()
print(tttt.mergeKLists([aaa, bbb, ccc]))