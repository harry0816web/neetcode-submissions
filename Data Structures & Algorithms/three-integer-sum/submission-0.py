class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        nums_len = len(nums)
        nums = sorted(nums)
        # print(nums)
        for i, num in enumerate(nums):
            target = num * -1
            l = 0
            r = nums_len - 1

            while r > l:
                # print("target: ", target, "l: ", nums[l], "r: ", nums[r])
                if l == i:
                    l += 1
                if r == i:
                    r -= 1
                    if r == l:
                        break

                if nums[l] + nums[r] == target:
                    ans = [nums[l], nums[r], num]
                    ans = tuple(sorted(ans))
                    ans_set.add(ans)
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else: r -= 1
        return_list = []
        for ans_list in ans_set:
            return_list.append(ans_list)

        return return_list
            