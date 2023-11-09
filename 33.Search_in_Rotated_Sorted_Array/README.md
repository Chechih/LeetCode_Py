# 33. Search in Rotated Sorted Array
### 問題
There is an integer array **nums** sorted in ascending order (with **distinct** values).

Prior to being passed to your function, **nums** is **possibly rotated** at an unknown pivot index **k (1 <= k < nums.length)** such that the resulting array is **[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed)**. For example, **[0,1,2,4,5,6,7]** might be rotated at pivot index 3 and become **[4,5,6,7,0,1,2]**.

Given the array **nums after** the possible rotation and an integer **target**, return the index of **target** if it is in **nums**, or **-1** if it is not in **nums**.

You must write an algorithm with **O(log n)** runtime complexity.

### 翻譯
給定一個升序排列的整數陣列 **nums**（具有 **不同** 的數值）。

在傳遞給你的函數之前，**nums** 可能已經在未知的旋轉中進行了旋轉，旋轉的軸心索引是 **k (1 <= k < nums.length)**，導致陣列的排列變為 **[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（從0開始索引）**。例如，**[0,1,2,4,5,6,7]** 可能在軸心索引 3 進行旋轉，變為 **[4,5,6,7,0,1,2]**。

給定在可能的旋轉後的整數陣列 **nums** 和一個整數 **target**，如果 **target** 存在於 **nums** 中，則返回其索引，否則返回 **-1**。

你必須編寫一個具有 **O(log n)** 運行時間複雜度的算法。

##### Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
##### Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
##### Example 3:
    Input: nums = [1], target = 0
    Output: -1

##### Constraints:
- 1 <= nums.length <= 5000
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

### 想法 1
暴力法，一個一個找XDDD
### 解法 1
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
```
### 想法 2
這題可以使用二分搜尋法，不過要使用有個難處，就是要判斷他在哪個地方旋轉了，但仔細觀察會發現陣列數值在往左移動時會使得最右邊的數字可能比中間還小，藉此可以判斷哪邊是有排序的，然後來找尋要往左邊找還是右邊找。
### 解法 2
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[right] >= nums[mid]:
                # 如果右邊比較大，代表右邊是有排序的[不是有迴旋的數列]
                if nums[mid] < target <= nums[right]:
                    # 且 target 被夾在中間
                    left = mid + 1
                else:
                    # 不然的話一定再另一邊
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
```