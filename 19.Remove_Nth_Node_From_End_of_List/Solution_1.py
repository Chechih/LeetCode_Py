from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        all_nodes = []
        node = head
        while node:
            all_nodes.append(node)
            node = node.next

        target = len(all_nodes) - n
        rlt = head
        if(target == 0):# 如果沒有前一個節點
            rlt = all_nodes[0].next
        elif(target != len(all_nodes) -1):
            all_nodes[target - 1].next = all_nodes[target + 1]
        else: # 如果是最後的節點，清掉
            all_nodes[target - 1].next = None
        return rlt


#測試
solution = Solution()
aaa = ListNode(1, ListNode(2))
print(solution.removeNthFromEnd(aaa, 2))