class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> um;
        for (int num : nums)
        {
            um[num]++;
        }
        std::map<int, std::vector<int>, std::greater<int>> om;
        for (auto p : um)
        {
            om[p.second].push_back(p.first);
        }
        std::vector<int> result;
        for (auto p : om)
        {
            for (int num : p.second)
            {
                if (result.size() == k)
                {
                    break;
                }
                result.push_back(num);
            }
        }
        return result;
    }
};
