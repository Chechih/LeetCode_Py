# 46. Permutations
### 問題
Given an array nums of distinct integers, return all the possible **permutations**. You can return the answer in **any order**.

### 翻譯
給定一個由不同整數組成的數組 nums，返回所有可能的**排列**。你可以以**任意順序**返回答案。

##### Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

##### Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

##### Example 3:
    Input: nums = [1]
    Output: [[1]]

##### Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are **unique**.

### 想法
使用遞歸遍歷每個元素，將其添加到當前排列中。
### 解法
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rlt = []
        def find_combination_sum(stack: List[int]) -> None:
            if(not nums):
                rlt.append(stack.copy())
            for i in range(len(nums)):
                stack.append(nums[i])
                temp = nums[i]
                nums.remove(temp)
                find_combination_sum(stack)
                nums.insert(i, temp)
                # 加回去 避免 for 迴圈炸掉 且才能檢查其他組合
                stack.pop()
```