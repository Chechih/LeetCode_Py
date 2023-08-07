class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)#轉字串
        str_x_leg = len(str_x)#字串長度
        left = str_x[:str_x_leg // 2]#字串左半邊
        right = str_x[str_x_leg // 2:] if str_x_leg % 2 == 0 else str_x[str_x_leg//2 + 1:]#字串右半邊
        return right[len(right)::-1] == left#右邊反轉比對香不相等
    

#測試
solution = Solution()
print(solution.isPalindrome(-121))