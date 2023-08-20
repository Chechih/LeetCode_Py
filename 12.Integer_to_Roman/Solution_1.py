class Solution:
    symbols = {# 對照表
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    def intToRoman(self, num: int) -> str:
        symbols = self.symbols
        rlt = ''
        for n, s in symbols.items():
            divide = num // n# 除除看，能除代表至少有一個此字母
            if divide != 0:
                for _ in range(divide):# 循環加字母
                    rlt += s
                num %= n

        return rlt

#測試
solution = Solution()
print(solution.intToRoman(58))