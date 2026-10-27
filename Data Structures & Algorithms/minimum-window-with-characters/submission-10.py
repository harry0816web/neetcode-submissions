class Solution:
    def minWindow(self, s: str, t: str) -> str:

        sz = len(s)

        if len(t) > len(s):
            return ""

        left = 0
        right = 0
        needed = {}

        # 記錄目前 window 還缺少幾個字元。
        # missing == 0 時，代表 window 有效。
        # 這樣不用每次都重新遍歷 target 檢查有效性。
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

            right = i

            if missing == len(t):
                left = i

            if needed[c] > 0:
                missing -= 1

            # 同一個 dictionary 同時記錄缺少和多餘的字元。
            # needed[c] < 0 代表 window 中有多餘的 c。
            needed[c] -= 1

            if needed[c] <= 0:
                if missing == 0:

                    # 只跳過多餘字元，不需要重新檢查整個 target。
                    idx = left

                    while idx < sz:
                        if s[idx] in needed:
                            if needed[s[idx]] < 0:
                                needed[s[idx]] += 1
                            elif needed[s[idx]] == 0:
                                break

                        idx += 1

                    left = idx

                    while s[left] not in needed:
                        left += 1

                    if (i - left + 1) < shortest_len:
                        shortest_len = i - left + 1
                        ans_l = left
                        ans_r = i

        if missing == 0 and (right - left + 1) < shortest_len:
            shortest_len = right - left + 1
            ans_l = left
            ans_r = right

        if ans_l == ans_r == -1:
            return ""

        return s[ans_l:ans_r + 1]