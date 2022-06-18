class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lp = 0, rp = nums.size(); int mid;
        while (rp - lp > 1) {
            mid = (rp + lp) >> 1;
            if (nums[mid] == target) return mid;
            (nums[mid] > target ? rp : lp) = mid;
        }
        return nums[lp] == target ? lp : -1;
    }
};