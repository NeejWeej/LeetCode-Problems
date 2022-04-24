class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        wrong_counts = p_c_len = len(p_c)
        cur_char = {}
        pLen = len(p)
        ans = []
        if pLen > len(s):
            return ans
        for idx, char in enumerate(s):
            # print(cur_char, wrong_counts)
            if idx >= pLen:
                old_char = s[idx - pLen] 
                cur_char[old_char] -= 1
                if cur_char[old_char] + 1 == p_c.get(old_char, 0):
                    wrong_counts += 1
                elif cur_char.get(old_char) == p_c.get(old_char, 0):
                    wrong_counts -= 1
                # print(idx, char, wrong_counts)
            cur_char[char] = cur_char.get(char, 0) + 1
            ccount = cur_char.get(char)
            if ccount == p_c.get(char, 0):
                wrong_counts -= 1
            if ccount -1 == p_c.get(char, 0):
                wrong_counts += 1
            if wrong_counts == 0:
                ans.append(1 + idx - pLen)
        return ans
                    
            
            
        