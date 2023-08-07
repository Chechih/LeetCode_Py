class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False# 從範例看起來, 負號一定不是, 直接不考慮
        comparison_val = 0# 反轉後的數字
        original_val = x# 原始值存一份
        while x > 0:# 開始翻轉數字
            comparison_val *= 10
            comparison_val += x % 10
            x //= 10
        return comparison_val == original_val# 如果翻轉後的數字和原始數字相等就是回文了
    

#測試
solution = Solution()
print(solution.isPalindrome(121))