class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):# 測試可能會只有一 直接回傳
            return s
        round_rule = 2* numRows - 2# 定義每幾個字元循環一次
        str_leg = len(s)# 字元長度
        rlt = ''#回傳值
        max_round = str_leg // round_rule + 2
        # 最多循環幾次 
        # 2是用來處理餘數部分的 
        # 因為剛好是零時不能跑回圈, 所以要有一, 然後結尾部分也要跑, 所以在加一, 
        # 多的部分會超出陣列, 所以不管他
        for j in range(0, max_round):
             #最上面
             ind = round_rule * j
             if(ind < str_leg):
                 rlt += s[ind]
        for i in range(1, numRows - 1):
            for j in range(0, max_round):
                #中間部分
                ind1 = round_rule * j - i# 中間部分可能多 i
                if(ind1 > 0 and ind1 < str_leg):
                    rlt += s[ind1]
                ind2 = round_rule * j + i
                if(ind2 > 0 and ind2 < str_leg):# 少 i
                    rlt += s[ind2]
        for j in range(0, max_round):
            #最下面
            ind = round_rule * j + round_rule // 2
            if(ind < str_leg):
                rlt += s[ind]
        return rlt

#測試
solution = Solution()
print(solution.convert("PAYPALISHIRING", 5))
print(solution.convert("ABCDE", 4))
print(solution.convert("PAYPALISHIRING", 3))
# print(solution.convert("ABCDE", 4))