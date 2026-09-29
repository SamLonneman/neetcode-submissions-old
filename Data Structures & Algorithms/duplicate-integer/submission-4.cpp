class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> m;
        for (int num : nums)
        {
            if (m.contains(num))
            {
                return true;
            }
            m[num]++;
        }
        return false;     
    }
};