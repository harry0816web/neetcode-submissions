class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # valid: map value <= target
        # invalid: shrink til map is valid
        # not in: clean map, then continue

        target = {}
        match = {}
        for c in s1:
            if c not in target:
                target[c] = 1
                match[c] = 0
            else:
                target[c] += 1

        print(target)

        left = 0
        for i, s in enumerate(s2):
            if s not in target:
                # use fromkeys build to get a map with 0s
                match = dict.fromkeys(target, 0)
                # we shrink left once invalid, but it must pass the valid state
                # so we can set left here
                left = i+1
            else:
                match[s] += 1
                # valid
                if match[s] <= target[s]:
                    #if match == original:
                        #left = i
                    if match == target:
                        return True
                # invalid
                else:
                    while match[s]> target[s]:
                        match[s2[left]] -= 1
                        left += 1

        return False

        

        

