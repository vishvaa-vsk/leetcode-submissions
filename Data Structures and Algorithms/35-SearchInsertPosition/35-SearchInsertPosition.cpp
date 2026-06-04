// Last updated: 6/4/2026, 6:37:07 PM
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start=0,end=nums.size();
        while(start<end){
            int mid=start+(end-start)/2;
            if(nums[mid]<target){
                start=mid+1;
            }
            else{
                end=mid;
            }
            
        }
        return start;
    }
};