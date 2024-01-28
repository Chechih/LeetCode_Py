
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        dp = [[False for i in range(len(s) + 1)] for j in range(p_leg + 1)]
        # 建 dp 用的陣列
        dp[0][0] = True
        for i in range(s_leg + 1):
            for j in range(1, p_leg + 1):# p 沒有字時，不可能匹配，直接不考慮
                if i - 1 >= 0 and p[j - 1] != '*':
                    dp[j][i] = dp[j - 1][i - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')
                    # 沒有 * 時，只能下去比對字串是不是相等，或是等於 ? 了
                elif p[j - 1] == '*':
                    dp[j][i] = dp[j - 1][i] or dp[j][i - 1]

        return dp[p_leg][s_leg]


solution = Solution()
print(solution.isMatch("aa","*"))


# solution = Solution()
# print(solution.isMatch("adceb","*a*b"))

# solution = Solution()
# print(solution.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))

# solution = Solution()
# print(solution.isMatch("abcabczzzde", "*abc???de*"))

solution = Solution()
print(solution.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))