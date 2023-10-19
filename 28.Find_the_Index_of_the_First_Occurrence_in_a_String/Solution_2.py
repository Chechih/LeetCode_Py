class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_leg = len(haystack)
        needle_leg = len(needle)
        for i in range(haystack_leg):
            if i + needle_leg > haystack_leg:
                # 如果加上去的長度比 haystack 直接跳出
                break 
            if haystack[i: i + needle_leg] == needle:
                # haystack[i: i + needle_leg] 是把跟 needle 一樣長的字串切出來比較
                # 如果相等就是所求
                return i
        return -1
            
solution = Solution()
print(solution.strStr("a", "a"))