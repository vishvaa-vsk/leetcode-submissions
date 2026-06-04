// Last updated: 6/4/2026, 6:38:03 PM
class Solution {
public:
    int myAtoi(string s) {
        long long int ans = 0;
        int size = s.size();
        int i = 0;
        bool isNeg = false;
        
        while(i < size && s[i] == ' ')
        {
            i++;
        }

        if (i < size && (s[i] == '+' || s[i] == '-'))
        {
            if (s[i] == '-') isNeg = true;
            i++;
        }

        while(i < size && ('0' <= s[i] && s[i] <= '9'))
        {
            ans = ans * 10 + (s[i] - '0');
            if (!isNeg && ans > INT_MAX) return INT_MAX;
            if (isNeg && -ans < INT_MIN) return INT_MIN;

            i++;
        }
        return isNeg ? -ans : ans;

    }
};