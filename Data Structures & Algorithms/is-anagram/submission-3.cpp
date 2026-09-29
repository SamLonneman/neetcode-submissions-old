class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;
        for (char c : s)
            s_map[c]++;
        for (char c : t)
            t_map[c]++;
        return s_map == t_map;
    }
};
