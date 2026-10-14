class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_cap = 0

        while r > l:
            lower = heights[r] if heights[r] <= heights[l] else heights[l]  # = min(...)
            cap = lower * (r-l)
            max_cap = max(cap, max_cap)
            if heights[r] >= heights[l]:
                l += 1
            else: r -= 1
        return max_cap