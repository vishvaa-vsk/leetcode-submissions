// Last updated: 6/4/2026, 6:35:46 PM
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> mpp;
        for(int i=0; i< nums.size(); i++){
            if (mpp.find(nums[i]) != mpp.end() && (i - mpp[nums[i]] <= k))
                return true;
            mpp[nums[i]] = i;
        }
        return false;
    }
};