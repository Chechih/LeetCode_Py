# 25. Reverse Nodes in k-Group
### 問題
Given the **head** of a linked list, reverse the nodes of the list **k** at a time, and return the modified list.

**k** is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of **k** then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Follow-up: Can you solve the problem in O(1) extra memory space?

 ### 翻譯
給定一個鏈結串列的**head**，將串列每 **k** 個節點一組地反轉，然後返回修改後的串列。

**k** 是一個正整數，且小於等於鏈結串列的長度。如果節點數量不是 **k** 的倍數，那麼剩餘的節點應該保持不變。

你不可以修改鏈結串列節點的值，只能更改節點本身。

後續問題：您能夠在額外的 **O(1)** 記憶體空間內解決這個問題嗎？
##### Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
![25. Reverse Nodes in k-Group Example 1](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg "25. Reverse Nodes in k-Group Example 1")  
圖片來源: [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)  
##### Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
![25. Reverse Nodes in k-Group Example 2](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg "25. Reverse Nodes in k-Group Example 2")  
圖片來源: [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)  

##### Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

### 想法 
這題一樣可以用物件共用記憶體的特性，先持續讀取 **鏈結串列**，並將結點存放在一個陣列(nodes)中，如果陣列大小等於 **k** 時，代表可以將裡面的節點翻轉了，不過需要注意的是，必須在用一個變數(previous_node)，來記錄上一次陣列(nodes)的最後一個節點(翻轉後的)，不然翻轉後的新 **鏈結串列** 的頭沒辦法接續上一次翻轉的 **鏈結串列**，最後就一直重複這動作到全部可以翻轉的都翻轉完畢即可。
### 解法 
```python
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
```