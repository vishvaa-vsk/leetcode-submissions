// Last updated: 6/4/2026, 6:36:27 PM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = nums[0];
        int total = 0;

        for (int n : nums) {
            if (total < 0) {
                total = 0;
            }
            total += n;
            res = max(res, total);
        }
        return res;        
    }
};