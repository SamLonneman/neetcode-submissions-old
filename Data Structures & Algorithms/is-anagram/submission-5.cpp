class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> m;
        for (char c : s)
        {
            m[c]++;
        }
        for (char c : t)
        {
            m[c]--;
        }
        for (auto p : m)
        {
            if (p.second)
            {
                return false;
            }
        }
        return true;
    }
};
