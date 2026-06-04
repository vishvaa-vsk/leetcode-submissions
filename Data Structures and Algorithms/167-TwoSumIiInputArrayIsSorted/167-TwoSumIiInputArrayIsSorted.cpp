// Last updated: 6/4/2026, 6:36:05 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        int sum = 0;
        while(l<r)
        {
            sum = numbers[l] + numbers[r];
            if (sum > target)
                r -= 1;
            else if(sum < target)
                l += 1;
            else
                return {l + 1, r + 1};
        }
        return {};
    }
};