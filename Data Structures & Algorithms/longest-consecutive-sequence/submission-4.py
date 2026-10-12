class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        num_set = set(nums)
        heads = []
        for num in nums:
            if num - 1 not in num_set:
                heads.append(num)
            
        if len(heads) == 1:
            return len(num_set)
        else:
            max_len = 0
            for head in heads:
                cnt_len = 1
                next_num = head + 1
                while next_num in num_set:
                    cnt_len += 1
                    next_num += 1
                
                max_len = max(max_len, cnt_len)
            
            return max_len
