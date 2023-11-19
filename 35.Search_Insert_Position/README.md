# 35. Search Insert Position
### 問題
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

### 翻譯
給定一個排列過的具有不同整數的陣列以及一個目標值，如果找到目標值，則返回其索引。如果未找到，則返回它應該插入的索引，以保持升序排序。

你必須編寫一個具有 **O(log n)** 運行時間複雜度的算法。

##### Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
##### Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
##### Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

##### Constraints:
- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- nums contains distinct values sorted in ascending order.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

### 想法
這題可以使用二分搜尋法來解決，只是一開始要先判斷是否超郭最大值或是低於最小值才開始尋找值。
### 解法
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # 先去頭尾這樣就不用特別判斷頭尾了
        while right - left > 1:
            # 一直尋找到相差一
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
```