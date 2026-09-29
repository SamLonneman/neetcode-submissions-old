class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> m;
        for (std::string str : strs)
        {
            std::vector<int> v(26, 0);
            for (char c : str)
            {
                v[c - 'a']++;
            }
            std::string s;
            for (int n : v)
            {
                s += n + ',';
            }
            m[s].push_back(str);
        }
        std::vector<std::vector<std::string>> result;
        for (auto p : m)
        {
            result.push_back(p.second);
        }
        return result;
    }
};
