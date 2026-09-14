class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        is_zero = 0
        for num in nums:
            if num == 0:
                is_zero += 1
            else:
                prod *= num
        
        ans = []
        for num in nums:
            if num == 0:
                if is_zero == 1:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                if is_zero:
                    ans.append(0)
                else:
                    ans.append(prod // num)
        return ans