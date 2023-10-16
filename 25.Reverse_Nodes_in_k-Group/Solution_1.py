from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseNodes(self, nodes: List[ListNode]) -> None:
        '''
        節點反向
        '''
        previous_node = None
        for i in range(len(nodes) - 1, -1, -1):
            n = nodes[i]
            if previous_node is not None:
                previous_node.next = n
            previous_node = n
        previous_node.next = None
        # 清除最後一個, 避免節點形成循環

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        rlt = None
        # 回傳用
        previous_node = None
        # 記錄每一組 k 的最後一個節點
        original_node = head
        while head:
            nodes.append(head)
            head = head.next
            if len(nodes) == k:
                self.reverseNodes(nodes)
                if rlt is None:
                    rlt = nodes[-1]
                if previous_node is not None:
                    previous_node.next = nodes[-1]
                previous_node = nodes[0]
                nodes = []
        if len(nodes) != 0:
            previous_node.next = nodes[0]
        if rlt is None:
            # 避免一組都沒有
            rlt = original_node
        return rlt


aaa = ListNode(1, ListNode(2))
solution = Solution()
print(solution.reverseKGroup(aaa, 2))