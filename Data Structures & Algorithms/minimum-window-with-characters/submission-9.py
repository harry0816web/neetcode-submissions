from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # One dictionary stores how many of each character are still needed.
        # Positive value: the window is missing characters.
        # Zero: the window has exactly enough.
        # Negative value: the window has extra copies.
        need = Counter(t)

        # Number of target characters still missing from the window.
        # This includes duplicates.
        missing = len(t)

        left = 0
        best_start = 0
        best_length = 100001

        for right, char in enumerate(s):
            # If this character was still needed, it satisfies one requirement.
            if need[char] > 0:
                missing -= 1

            # Decrease the count:
            # - positive -> fewer required characters remain
            # - zero -> exactly enough copies
            # - negative -> this is an extra character
            need[char] -= 1

            # The window contains all characters required by t.
            # We do not rescan every key in need; missing == 0 is enough.
            while missing == 0:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                # Remove the leftmost character before shrinking further.
                left_char = s[left]
                need[left_char] += 1

                # If the count becomes positive, we removed a required
                # character, so the window is no longer valid.
                if need[left_char] > 0:
                    missing += 1

                left += 1

        if best_length == 100001:
            return ""

        return s[best_start:best_start + best_length]