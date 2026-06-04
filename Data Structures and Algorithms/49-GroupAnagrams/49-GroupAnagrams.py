# Last updated: 6/4/2026, 6:36:36 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(s)

        return list(result.values())
        