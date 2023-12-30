# 42. Trapping Rain Water
### 問題
Given **n** non-negative integers representing an elevation map where the width of each bar is **1**, compute how much water it can trap after raining.

### 翻譯
給定 **n** 個非負整數，這些整數代表一個高程圖，其中每個柱子的寬度為 **1**，計算下雨後它能夠捕捉多少水。

##### Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
![Question_42_Example1](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png "question_42_example1")  
圖片來源 LeetCode

##### Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

##### Constraints:
- n == height.length
- 1 <= n <= 2 * 10<sup>4</sup>
- 0 <= height[i] <= 10<sup>5</sup>

### 想法 1
這道題目想法是建立 left_height 和 right_height，將左右兩邊最高的高度都先記下來，然後再去比對左右兩邊高度最小值和現在最小值的差值總和及所求。
### 解法 1
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        height_leg = len(height)
        left_height = [0] * height_leg
        right_height = [0] * height_leg
        left_height[0] = height[0]
        right_height[height_leg - 1] = height[height_leg - 1]
        for i in range(1, height_leg):
            # 先找出所有的左邊
            left_height[i] = max(left_height[i - 1], height[i])

        for i in range(height_leg - 2, -1, -1):
            # 再找出所有的右邊
            right_height[i] = max(height[i], right_height[i + 1])   

        rlt = 0
        for i in range(1, height_leg - 1):
            # 比較每個位子的左右兩邊並減去現在高度，就是當前的水量
            rlt += min(left_height[i], right_height[i]) - height[i]

        return rlt
```
### 想法 2
這想法其實和 **想法 1** 類似，只是多了要用雙指標，去比對左右兩邊的高度哪邊比較高，然後再去算差值。
### 解法 2
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        height_leg = len(height)

        left, right = 0, height_leg - 1
        left_max, right_max = height[left], height[right]
        rlt = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                rlt += left_max - height[left]
                left += 1
            else:
                rlt += right_max - height[right]
                right -= 1

        return rlt
```