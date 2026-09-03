class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cha_s, cha_t = {}, {}
        for cha in s:
            if cha in cha_s:
                cha_s[cha] += 1
            else:
                cha_s[cha] = 1

        for cha in t:
            if cha in cha_t:
                cha_t[cha] += 1
            else:
                cha_t[cha] = 1
            
        return cha_s == cha_t
