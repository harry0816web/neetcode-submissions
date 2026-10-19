class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        # warmer_idx = [0]*len(temperatures)
        # for i, temp in enumerate(temperatures):
        #     for j in range(0, i):
        #         if temp > temperatures[j] and warmer_idx[j] == 0:
        #             warmer_idx[j] = i - j

        # return warmer_idx

        class Day:
            def __init__(self, idx, temp):
                self.idx = idx
                self.temp = temp

        warmer_idx = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if i != 0:
                # check stack not empty
                while stack and temp > stack[-1].temp:
                    warmer_idx[stack[-1].idx] = i - stack[-1].idx
                    # stack might be popped to empty
                    stack.pop()

            stack.append(Day(i, temp))                                  
            # stack = sorted(stack, key=lambda d: d.temp, reverse = True)

        return warmer_idx

