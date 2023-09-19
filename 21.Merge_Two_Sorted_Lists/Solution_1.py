from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        newList = ListNode()
        rlt = newList
        previous = newList # 清除掉最後面多餘的節點用的
        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                newList.val = list1.val
                list1 = list1.next
            else:
                newList.val = list2.val
                list2 = list2.next
            previous = newList
            newList.next = ListNode()
            newList = newList.next
        if previous:
            previous.next = None

        return rlt