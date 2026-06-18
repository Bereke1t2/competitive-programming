class Solution {
public:
    int maximumStrongPairXor(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        int i = 0, ans = 0;

        for (int j = 0; j < n; j++) {
            // maintain valid window
            while (nums[j] > 2 * nums[i]) {
                i++;
            }

            // check all pairs with current j
            for (int k = i; k < j; k++) {
                ans = max(ans, nums[j] ^ nums[k]);
            }
        }

        return ans;
    }
};