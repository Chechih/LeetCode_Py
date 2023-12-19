from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_leg = len(nums)

        # 1. 以特殊標記編號 (n+1) 標記編號 (num < 0) 和 (num > n)
        # （我們可以忽略這些，因為如果所有數字都 > n 那麼我們將簡單地傳回 1）
        for i in range(nums_leg):
            if nums[i] <= 0 or nums[i] > nums_leg:
                nums[i] = nums_leg + 1

        # 數組中的所有數字現在都是正數，且範圍為 1..n+1
    
        # 2. 透過將該數字的索引轉換為負數來標記數組中出現的每個單元格
        for i in range(nums_leg):
            num = abs(nums[i])
            if num > nums_leg:
                continue
            num -= 1
            # -1 表示基於零索引的陣列（因此數字 1 將位於位子 0）
            if nums[num] > 0:
                # 防止雙重否定運算
                nums[num] = -1 * nums[num]
            
        # 3.找出第一個非負數的儲存格（沒有出現在陣列中）
        for i in range(nums_leg):
            if nums[i] >= 0:
                return i + 1
    
        # 4. 沒有找到正數，這表示數組包含所有數字 1..n
        return nums_leg + 1

slution = Solution()
print(slution.firstMissingPositive([1]))