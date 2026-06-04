// Last updated: 6/4/2026, 6:38:01 PM
class Solution {
public:
    bool isPalindrome(int x) {
        long rev = 0;
        int temp = x;
        if(x < 0)
            return false;
        while(x > 0)
        {
            rev = (rev*10)+ x%10;
            x/=10;
        }
        return temp==rev;
    }
};