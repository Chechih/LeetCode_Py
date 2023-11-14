# 34. Find First and Last Position of Element in Sorted Array
### 問題
Given an array of integers **nums** sorted in non-decreasing order, find the starting and ending position of a given **target** value.

If **target** is not found in the array, return **[-1, -1]**.

You must write an algorithm with **O(log n)** runtime complexity.

### 翻譯
給定一個以非遞減順序排列的整數陣列 **nums**，找到給定的 **target** 值的起始和結束位置。

如果在陣列中找不到 **target**，則返回 **[-1, -1]**。

你必須編寫一個具有 **O(log n)** 運行時間複雜度的算法。

##### Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
##### Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
##### Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

##### Constraints:
- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- nums is a non-decreasing array.
- -10<sup>9</sup> <= target <= 10<sup>9</sup>

### 想法 1
這題是給個排序好的陣列，去找特定值(target)出現的範圍。
這樣的話可以使用二分搜尋法，先找到最左邊的 target ，然後再二分搜尋法找最右邊的 target，而第二次時，
可以讓第一次找到的位子當二分搜尋法初始 left 的位子，先過濾掉一些，再開始第二次搜尋。
### 解法 1
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        mid = 0
        rlt = [-1, -1]
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                if (mid == 0 or nums[mid -1] < nums[mid]):
                    # 找左邊
                    rlt[0] = mid
                    break
                else:
                    right -= 1
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        if rlt[0] == -1:
            return rlt
        left = rlt[0]
        # 因為上面找到了 直接用他繼續找
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid +1] > nums[mid]:
                    # 找右邊
                    rlt[1] = mid
                    break
                else:
                    left += 1
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return rlt
```
### 想法 2
再來也可以用 index 和 count，直接找出來範圍，反正題目沒說不能用(?
### 解法 2
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target in nums):
            start = nums.index(target)
            return [start, start + nums.count(target) - 1]
        return [-1, -1]
```