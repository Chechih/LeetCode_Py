from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_vals = []
        for i in range(len(lists)):
            l = lists[i]
            while(l != None):
                all_vals.append(l.val)
                l = l.next
        if len(all_vals) == 0:
            return None
        all_vals.sort()
        all_vals.reverse()
        rlt = ListNode()
        rlt.val = all_vals.pop()
        rlt.next = None
    
        new_node = rlt
        while len(all_vals) > 0:
            new_node.next = ListNode()
            new_node = new_node.next
            new_node.val = all_vals.pop()
            new_node.next = None
        
        return rlt
        

aaa = ListNode(0, ListNode(2, ListNode(4)))
bbb = ListNode(1, ListNode(3, ListNode(4)))
ccc = ListNode(5, ListNode(6))
ddd = ListNode(None)

tttt = Solution()
print(tttt.mergeKLists([aaa, bbb, ccc]))