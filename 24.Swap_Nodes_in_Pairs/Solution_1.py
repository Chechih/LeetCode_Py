from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        # 紀錄上一個節點
        rlt = head
        # 回傳用的
        while head:
            if not previous_node:
                temp = head.val
                head.val = previous_node.val
                previous_node.val = temp
                # 換值
                previous_node = None
            else:
                previous_node = head
            head = head.next
        return rlt
