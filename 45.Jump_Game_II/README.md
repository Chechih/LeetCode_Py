# 45. Jump Game II
### 問題
You are given a **0-indexed** array of integers **nums** of length **n**. You are initially positioned at **nums[0]**.

Each element **nums[i]** represents the maximum length of a forward jump from index **i**. In other words, if you are at **nums[i]**, you can jump to any **nums[i + j]** where:

- **0 <= j <= nums[i]** and
- **i + j < n**
Return the minimum number of jumps to reach **nums[n - 1]**. The test cases are generated such that you can reach **nums[n - 1]**.

### 翻譯
給定一個長度為 **n** 的整數陣列 **nums**（下標從0開始）。你最初位於 **nums[0]**。

每個元素 **nums[i]** 表示從索引 **i** 出發的最大跳躍長度。換句話說，如果你在 **nums[i]**，你可以跳到任何 **nums[i + j]**，其中：

- 0 <= j <= nums[i] 且
- i + j < n
返回到達 **nums[n - 1]** 的最小跳躍次數。測試案例保證你可以到達 **nums[n - 1]**。

##### Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

##### Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

##### Constraints:
- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].

### 想法 1
這題可以使用動態規劃的方式來解決，可以歸類成以下步驟:  
1. 設定 max_num 為 10000，用來表示不可能底達的情形。
2. 創建一個陣列 step_dict 用來記錄每個位置到達終點的最小步數。
3. 如果 nums 為 1，表示已經在終點，直接返回 0 。
4. 使用迴圈從陣列[nums]的最後一個位置開始向前遍歷。
5. 對於每一個位置 i，計算從該位置到終點的最小步數。
6. 如果 i + nums[i] >= nums_leg - 1，表示從該位置，走一步即可到達終點，將 step_dict[i] 設定為 1。
7. 如果 max_move == 0，表示無法到達終點，將 step_dict[i] 設定為 max_num。否則，將 step_dict[i] 設定為從位置 i + 1 到 i + max_move 的最小步數加上 1。
8. 重複步驟 5 到陣列結束
9. 最後返回 step_dict[0]，即從起始位置到達終點的最小步數。
### 解法 1
```python
class Solution:
    max_num = 10000
    def jump(self, nums: List[int]) -> int:
        nums_leg = len(nums)
        step_dict = [0] * nums_leg
        # 紀錄這個位子到終點的最少歩數
        if(nums_leg == 1):
            # 在終點上不用走了
            return 0
        # 設定最大值用的
        for i in range(nums_leg - 1, -1, -1):
            max_move = nums[i]
            if(i + max_move >= nums_leg -1):
                # 超過終點直接紀錄 1 步
                step_dict[i] = 1
            elif(max_move == 0):
                # 不可能到達
                step_dict[i] = self.max_num
            else:
                step_dict[i] = min(step_dict[i + 1: i + max_move + 1]) + 1
                # 計算最小步數
        return step_dict[0]
```
### 想法 2
網路上搜尋其他人的做法，發現也可以使用貪婪演算法。再每次選擇當前能夠到達的範圍內，選擇能夠跳得更遠的位置，這樣可以最小化步數。在每次跳躍到當前範圍的最遠位置時，更新範圍的結束位置，繼續遍歷直到終點。
### 解法 2
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_position = 0
        # 找能跳最遠的
        steps = 0
        for i in range(len(nums) - 1):
            max_position = max(max_position, nums[i] + i)
            if(i == end):
                # 遇到最大長度，就更新長度，步數加一
                end = max_position
                steps += 1
        return steps
```