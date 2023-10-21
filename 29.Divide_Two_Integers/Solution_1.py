class Solution:
    MAX_LIMIT = 2147483647
    MIN_LIMIT = -2147483648
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if dividend == self.MIN_LIMIT and divisor == -1:
            return self.MAX_LIMIT
        # 因為只有可能最小值是溢位的狀況
        if dividend < 0 or divisor < 0:
            is_negative = not (dividend < 0 and divisor < 0)
            dividend = abs(dividend)
            divisor = abs(divisor)
        # 判斷負數
        
        dic = []
        multiple = 1
        add = divisor
        while(dividend >= add):
            dic.append((multiple, add))
            multiple = multiple + multiple
            add = add + add
        # 找 divisor 的倍數
        rlt = 0
        dic = dic[::-1]
        # 翻轉後才能從大的開始減

        for (multiple, add) in dic:
            if dividend - add >= 0:
                rlt += multiple
                dividend -= add
        rlt = -rlt if is_negative else rlt 
        return rlt


solution = Solution()
solution.divide(-55, -3)