class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        last = {}
        max_len = 0

        # need to maintain in the window
        # window
        left = 0
        right = 0
        # cound most frequent cha
        freq = {}
        max_f = 0
        # when window sz - most freq > k, window turns to invalid, shrink left til it's valid again
        left = 0
        max_len = 0

        for right, c in enumerate(s):
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

            max_f = max(freq[c], max_f)

            while (right - left + 1) - max_f > k:
                if freq[s[left]] - 1 >= 0:
                    freq[s[left]] -= 1
                else:
                    freq.pop(s[left])
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len