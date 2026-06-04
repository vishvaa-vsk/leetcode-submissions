# Last updated: 6/4/2026, 6:38:15 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = float("-inf")
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l+=1
            result = max(result, r-l+1)
        
        return result if result != float("-inf") else 0

