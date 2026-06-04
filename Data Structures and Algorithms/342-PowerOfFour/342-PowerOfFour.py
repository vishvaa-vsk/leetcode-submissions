# Last updated: 6/4/2026, 6:35:30 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n-1)) == 0 and n % 3 == 1
        