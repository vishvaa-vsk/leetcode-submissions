// Last updated: 6/4/2026, 6:37:16 PM
class Solution {
public:
    int findDip(vector<int> nums, int idx) {
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                return i;
            }
        }
        return idx;
    }

    void nextPermutation(vector<int>& nums) {
        int index = findDip(nums, -1);

        if (index == -1) {
            reverse(nums.begin(), nums.end());
            return;
        }
        for (int i = nums.size() - 1; i > index; i--) {
            if (nums[i] > nums[index]) {
                swap(nums[i], nums[index]);
                break;
            }
        }
        reverse(nums.begin() + index + 1, nums.end());
    }
};