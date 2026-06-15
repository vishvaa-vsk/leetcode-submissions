# Last updated: 16/06/2026, 00:11:01
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l,r = 0, len(s)-1
4        while (l < r):
5            while (l < r and not s[l].isalnum()):
6                l += 1
7            while (l < r and not s[r].isalnum()):
8                r -= 1
9            if s[l].lower() == s[r].lower():
10                l += 1
11                r -= 1
12            else:
13                return False
14        return True