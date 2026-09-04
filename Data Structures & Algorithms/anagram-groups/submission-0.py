class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap { hashmap -> idx }
        group_idx = 0
        anagram_group = {}
        groups = []
        for string in strs:
            chas = [0] * 26
            for cha in string:
                chas[ord(cha) - ord('a')] += 1
            
            key = tuple(chas)
            if key not in anagram_group:
                anagram_group[key] = group_idx
                groups.append([string])
                group_idx += 1
            else:
                groups[anagram_group[key]].append(string)

        return groups