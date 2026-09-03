class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterpart = {}
        for idx, num in enumerate(nums):
            residual = target - num
            if residual in counterpart:
                return [counterpart[residual], idx]


            if num not in counterpart:
                counterpart[num] = idx

            
