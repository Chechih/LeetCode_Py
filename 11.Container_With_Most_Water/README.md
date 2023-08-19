# 11. Container With Most Water
### 問題
You are given an integer array **height** of length **n**. There are **n** vertical lines drawn such that the two endpoints of the **i<sup>th</sup>** line are **(i, 0)** and **(i, height[i])**.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.
 ### 翻譯
您被給定一個長度為 **n** 的整數陣列 **height**。有 **n** 條垂直線，使得**第 i 條線**的兩個端點分別為 **(i, 0)** 和 **(i, height[i])**。

找到兩條線，它們與 x 軸一起形成一個容器，使得該容器能夠包含最多的水。

返回容器能夠儲存的最大水量。

**請注意**，您不能傾斜容器。
##### Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
![Question_11_Example1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg "question_11_example1")  
圖片來源 LeetCode
##### Example 2:
    Input: height = [1,1]
    Output: 1
##### Constraints:
- n == height.length
- 2 <= n <= 10<sup>5</sup>
- 0 <= height[i] <= 10<sup>4</sup>

### 想法 
其實這題一開始，我是用暴力破解法的，沒辦法過XDDD
然後觀察下，其實這題就是要找最大面積，而他的面積，其實就是由兩個因素決定的:  
1. 下排的寬度(位子相減)  
2. 高度最小值(height 的值)  
所以可以使用雙指標，從左右兩側跑，當指標互相靠近時，盡可能地去找出更大的 height ，去補償寬度邊小
### 解法 
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_leg = len(height)
        left = 0
        right = height_leg - 1
        max_area = 0# 存最大面積
        while left < right:
            area = 0
            if height[left] <  height[right]:# 右邊己較高時
                area = height[left] * (right - left)# 左邊當高
                left += 1
            else:# 左邊己較高時
                area = height[right] * (right - left)# 右邊當高
                right -= 1
            max_area = max(max_area, area)

        return max_area
```