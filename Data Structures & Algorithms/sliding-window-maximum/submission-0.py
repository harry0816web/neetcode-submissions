from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # indices; their values are strictly decreasing
        res = []

        for i, n in enumerate(nums):
            # 1. remove index that fell out of the window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # 2. remove smaller values from the back
            while dq and nums[dq[-1]] <= n:
                dq.pop()
            # 3. add current index
            dq.append(i)
            # 4. record max once the window is full
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res