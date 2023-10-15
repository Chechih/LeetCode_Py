# 24. Swap Nodes in Pairs
### 問題
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 ### 翻譯
給定一個鏈結串列，交換每兩個相鄰的節點，然後返回新的鏈結串列的頭部。你必須在不修改鏈結串列節點的值的情況下解決這個問題（即只能更改節點本身）。
##### Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
![24. Swap Nodes in Pairs Example 1](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg "24. Swap Nodes in Pairs Example 1")  
圖片來源: [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)  
##### Example 2:
    Input: head = []
    Output: []
##### Example 3:
    Input: head = [1]
    Output: [1]

##### Constraints:
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

### 想法 
這題可以用物件共用記憶體的特性，用一個變數(previous_node)紀錄基數節點物件，偶數節點時，和 previous_node 裡面存放的物間交換值，並清空 previous_node，一直到把整個**鏈結串列**跑完即可。
### 解法 
```python
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
```