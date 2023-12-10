
class Solution:
    def countAndSay(self, n: int) -> str:
        rlt = '1'
        for _ in range(2, n + 1):
            res = ''
            val = rlt[0]
            count = 0
            for s in rlt:
                if(val == s):
                    count += 1
                    # 累加
                else:
                    res += str(count) + val
                    # 開始說數字
                    val = s
                    count = 1
                    # 初始
            res += str(count) + val
            rlt = res
            # 記錄每一輪的值

        return rlt




solution = Solution()
print(solution.countAndSay(5))