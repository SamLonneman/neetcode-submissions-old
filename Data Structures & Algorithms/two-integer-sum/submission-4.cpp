class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++)
        {
            if (m.contains(nums[i]))
            {
                return std::vector<int>({m[nums[i]], i});
            }
            m[target - nums[i]] = i;
        }
    }
};
