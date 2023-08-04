class Solution:
    max_size = 2 ** 31 - 1#32 位元最大值
    min_size = -max_size - 1 #32 位元最小值
    def reverse(self, x: int) -> int:
        rlt = 0
        abs_x = abs(x)
        is_positive = x > 0
        max_size_divide10 = self.max_size / 10#32 位元最大值除10
        min_size_divide10 = self.min_size / 10
        while(abs_x != 0):
            abs_x_mod10 = abs_x % 10 if is_positive else -(abs_x % 10)
            if max_size_divide10 < rlt + abs_x_mod10 / 10:#檢查加上去是不是比最大值大
                return 0
            if rlt + abs_x_mod10 / 10 < min_size_divide10:#檢查加上去是不是比最小值小
                return 0
            rlt = rlt *10 + abs_x_mod10#檢查通過直接加
            abs_x = abs_x //10

        return rlt
#測試
solution = Solution()
print(solution.reverse(-123))
print(solution.reverse(1534236469))