from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        is_check_ok = set()
        # 將檢查過可以的字串存起來
        is_check_no = set()
        # 將檢查過不可以的字串存起來
        def split_list(text, leg) -> List[str]:
            rlt = [text[idx : idx + leg] for idx in range(0, len(text), leg)]
            rlt.sort()
            return rlt
        def run():
            all_words_leg = len(''.join(words))
            if all_words_leg == 0:
                return []
            word_leg = len(words[0])
            #因為題目有說 words 內的 word 長度相等
            s_leg = len(s)
            words.sort()
            rlt = []
            for i in range(s_leg - all_words_leg + 1):
                spilt_str = s[i: i + all_words_leg]
                if spilt_str in is_check_ok:
                    rlt.append(i)
                    continue
                elif spilt_str in is_check_no:
                    continue
                split_str_list = split_list(spilt_str, word_leg)
                if split_str_list == words:
                    #因為排序過了, 如果相等代表是所求的東西
                    rlt.append(i)
                    is_check_ok.add(spilt_str)
                else:
                    is_check_no.add(spilt_str)
            return rlt
        return run()
    
solution = Solution()
solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
