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
        target = {}
        match = {}
        new_window = True
        ans_l = -1
        ans_r = -1
        for c in t:
            if c not in target:
                match[c] = 0
                target[c] = 1
            else:
                target[c] += 1

        shortest_len = 100001
        for i, c in enumerate(s):
            if c not in target:
                continue
            else:
                right = i
                if new_window:
                    left = i
                    new_window = False

                match[c] += 1
                if match[c] >= target[c]:
                    # shrink if having at least freq of target
                    at_least = True
                    for key, vals in target.items():
                        if match[key] < target[key]:
                            at_least = False
                            break
                    if at_least:
                        print("at least: ", s[i])
                        # shrink window
                        idx = left
                        while idx < sz:
                            if s[idx] in target:
                                if match[s[idx]] > target[s[idx]]:
                                    match[s[idx]] -= 1
                                elif match[s[idx]] == target[s[idx]]:
                                    print("tied: ", s[idx:i + 1])
                                    break
                            idx += 1

                        left = idx
                        
                        while s[left] not in target:
                            left += 1
                        print("match found:")
                        print(s[left: i+1])
                        if (i - left + 1) < shortest_len:
                            shortest_len = (i - left + 1)
                            ans_l = left
                            ans_r = i
                        # while match[c] > target[c]:
                        #     if s[idx] not in target:
                        #         idx += 1
                        #         continue
                        #     else:
                        #         match[s[idx]] -= 1
                        #         idx += 1
                        #     # find next valid
                        #     while s[idx] not in target:
                        #         idx += 1
                        #     left = idx


        if match == target and (right - left + 1) < shortest_len:
            print("match found:")
            print(s[left: right+1])
            shortest_len = (right - left + 1)
            ans_l = left
            ans_r = right

        if ans_l == ans_r == -1:
            return ""
        return s[ans_l:ans_r+1]
