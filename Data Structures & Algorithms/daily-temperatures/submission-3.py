class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        # warmer_idx = [0]*len(temperatures)
        # for i, temp in enumerate(temperatures):
        #     for j in range(0, i):
        #         if temp > temperatures[j] and warmer_idx[j] == 0:
        #             warmer_idx[j] = i - j

        # return warmer_idx

        # No need to create class for id <-> temp
        # Just store id to lookup for temp
        # class Day:
        #     def __init__(self, idx, temp):
        #         self.idx = idx
        #         self.temp = temp

        warmer_idx = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # check stack not empty
            while stack and temp > temperatures[stack[-1]]:
                warmer_idx[stack[-1]] = i - stack[-1]
                # stack might be popped to empty
                stack.pop()
                

            stack.append(i)                                  
            # stack = sorted(stack, key=lambda d: d.temp, reverse = True)

        return warmer_idx

