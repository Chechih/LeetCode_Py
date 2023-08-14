# 先載入正規表達式的套件 re (Regular Expressions)
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        finded = re.findall(p, s)
        return len(finded) > 0 and finded[0] == s

tttt = Solution()
print(tttt.isMatch("aa", "a*"))