class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}       # char -> last index seen
        left = 0
        max_len = 0
        for i, c in enumerate(s):
            # condition to udpate window left:
            # 1. duplicate found, shrink window
            # 2. left might be updated since last seen c
            #    so make sure last[c] + 1 is bigger than left
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = i
            # Don't need "right", window grows in each step, 
            # only shrink need consideration
            max_len = max(max_len, i - left + 1)
        return max_len

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substr = {}
#         left = 0
#         right = 0
#         if len(s) <= 1:
#             return len(s)

#         # if cha not in substr: right grow
#         # if cha in substr: left changes to substr.find(cha) + 1
        
#         max_len = 0
#         for i, cha in enumerate(s):
#             if cha not in substr:
#                 substr[cha] = i
#                 right = i
#             else:
#                 # print(cha, "already in hashmap")
#                 max_len = max(max_len, right - left + 1)
#                 if substr[cha] + 1 > left:
#                     left = substr[cha] + 1 
#                 substr[cha] = i
#                 right = i
#                 # print("after: ")
#                 # print("left: ", left, "right: ", right)

                        
#         max_len = max(max_len, right - left + 1)


#         return max_len