class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        sz = len(prices)
        max_prof = 0
        for i in range(1, sz):
            if prices[i] > prices[left]:
                if prices[i] > prices[right]:
                    right = i
                    print("right: ", prices[i])
            else:
                max_prof = max(max_prof, prices[right] - prices[left])
                left = i
                right = i
                print("left: ", left)

        max_prof = max(max_prof, prices[right] - prices[left])
        return max_prof
        