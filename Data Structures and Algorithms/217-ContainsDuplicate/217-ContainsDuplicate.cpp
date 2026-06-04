// Last updated: 6/4/2026, 6:36:01 PM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;

        for(auto num: nums)
        {
            set.emplace(num);
        }

        if(set.size() < nums.size())
            return true;
        else
            return false;
    }
};