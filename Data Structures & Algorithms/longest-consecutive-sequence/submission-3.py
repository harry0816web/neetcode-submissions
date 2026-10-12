class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums = sorted(nums)
        cnt_len = 1
        max_len = 0
        for (i, num) in enumerate(nums):
            if i == 0: continue

            if num == nums[i-1]:
                continue
            elif num == nums[i-1] + 1:
                cnt_len += 1
                max_len = max(max_len, cnt_len)
            else:
                max_len = max(max_len, cnt_len)
                cnt_len = 1

        return 1 if max_len == 0 else max_len