class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = {}
        left = 0
        right = 0
        if len(s) <= 1:
            return len(s)

        # if cha not in substr: right grow
        # if cha in substr: left changes to substr.find(cha) + 1
        
        max_len = 0
        for i, cha in enumerate(s):
            if cha not in substr:
                substr[cha] = i
                right = i
            else:
                # print(cha, "already in hashmap")
                max_len = max(max_len, right - left + 1)
                if substr[cha] + 1 > left:
                    left = substr[cha] + 1 
                substr[cha] = i
                right = i
                # print("after: ")
                # print("left: ", left, "right: ", right)

                        
        max_len = max(max_len, right - left + 1)


        return max_len