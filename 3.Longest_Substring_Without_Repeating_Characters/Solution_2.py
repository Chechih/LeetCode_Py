class Solution:
    def lengthOfLongestSubstring(self, s: str):
        numset = set()#存出現過的字元
        left = 0#現在出現過的最常字元初始位子
        max_rlt = 0
        for i, char in enumerate(s):
            while char in numset:#如果現在的字元在之前找到的字串上，一直往右移，直到都沒有
                numset.remove(s[left])
                left += 1
            numset.add(char)
            max_rlt = max(max_rlt, i - left + 1)
        return max_rlt
#測試
solution = Solution()
solution.lengthOfLongestSubstring("abacabbda")