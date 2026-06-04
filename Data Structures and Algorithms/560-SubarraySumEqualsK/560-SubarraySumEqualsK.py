# Last updated: 6/4/2026, 6:35:29 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        freq = {0:1}

        for num in nums:
            current_sum += num
            if current_sum -k in freq:
                count += freq[current_sum - k]
            freq[current_sum] = freq.get(current_sum,0)+1
        
        return count
        
