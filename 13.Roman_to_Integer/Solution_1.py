class Solution:
    symbols = {# 對照表
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        symbols = self.symbols
        rlt = 0
        prev_val = 0# 上一個值
        for c in s:
            val = symbols[c]
            if val > prev_val:
                # 如果現在的數字比上個大，代表可能是 4(IV) 9(IX)，這種要減去的羅馬數字
                rlt -= 2 * prev_val
                # 減 2 倍是因為上一個回圈是加的，扣掉
            rlt += val
            prev_val = val
        return rlt

#測試
solution = Solution()
print(solution.romanToInt("MCMXCIV"))