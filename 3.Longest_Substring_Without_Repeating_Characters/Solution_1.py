class Solution:
    def lengthOfLongestSubstring(self, s: str):
        charCount = len(s)
        spilt = ''#紀錄這個字串到下個重複的字串的變數
        max_rlt = 1 if charCount > 0 else 0#初始回傳 max_rlt
        for i, char in enumerate(s): 
            spilt = char
            for j in range(i + 1, charCount):
                char = s[j]
                if(char in spilt):#如果在切的字串內(重複了)
                    break
                else:
                    spilt += char
                max_rlt = max(max_rlt, len(spilt))#抓最大的  
        return max_rlt
    

#測試
solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")