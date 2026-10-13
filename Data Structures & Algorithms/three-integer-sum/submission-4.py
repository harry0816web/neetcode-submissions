class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        nums_len = len(nums)
        nums = sorted(nums)
        for i, num in enumerate(nums):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = num * -1
            # only check those > nums[i] to prevent duplicate
            l = i+1
            r = nums_len - 1

            while r > l:
                if nums[l] + nums[r] == target:
                    # cuz we've sorted, the order is certain
                    ans = [num, nums[l], nums[r]]
                    ans = tuple(ans)
                    ans_set.add(ans)
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else: r -= 1

        return_list = []
        for ans_list in ans_set:
            return_list.append(ans_list)

        return return_list
            