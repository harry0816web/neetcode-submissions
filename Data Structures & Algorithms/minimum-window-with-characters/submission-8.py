class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # what to maintain
            # left (index of first cha in target)
            # hashmap to count duplicates
            # when found a extra c 
            # compare length 
            # -> shrink window till valid again, start a new window

        sz = len(s)
        if len(t) > len(s):
            return ""
        left = 0
        right = 0
        needed = {}
        # counter for missing character, turn O(k) valid check to O(1)
        missing = len(t)
        new_window = True
        ans_l = -1
        ans_r = -1
        for c in t:
            if c not in needed:
                needed[c] = 1
            else:
                needed[c] += 1

        shortest_len = 100001
        for i, c in enumerate(s):
            if c not in needed:
                continue
            else:
                right = i
                if missing == len(t):
                    left = i

                # if c still needed, missing -= 1
                if needed[c] > 0:
                    missing -= 1
                    # print("c: ", c)

                needed[c] -= 1
                if needed[c] <= 0:
                    if missing == 0:
                        print("at least: ", s[i])
                        # shrink window
                        idx = left
                        while idx < sz:
                            if s[idx] in needed:
                                if needed[s[idx]] < 0:
                                    needed[s[idx]] += 1
                                elif needed[s[idx]] == 0:
                                    # print("tied: ", s[idx:i + 1])
                                    break
                            idx += 1

                        left = idx
                        
                        while s[left] not in needed:
                            left += 1
                        # print("match found:")
                        # print(s[left: i+1])
                        if (i - left + 1) < shortest_len:
                            shortest_len = (i - left + 1)
                            ans_l = left
                            ans_r = i


        if missing == 0 and (right - left + 1) < shortest_len:
            # print("match found:")
            # print(s[left: right+1])
            shortest_len = (right - left + 1)
            ans_l = left
            ans_r = right

        if ans_l == ans_r == -1:
            return ""
        return s[ans_l:ans_r+1]
