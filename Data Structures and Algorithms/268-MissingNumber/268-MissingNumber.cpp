// Last updated: 6/4/2026, 6:35:40 PM
class Solution {
public:
    int missingNumber(vector<int>& nums)
    {
        int Xor = 0;
        for(int i=0; i<= nums.size(); i++)
        {
            Xor ^= i;
        }
        for(int i=0; i < nums.size(); i++)
        {
            Xor ^= nums[i];
        }

        return Xor;
    }
};