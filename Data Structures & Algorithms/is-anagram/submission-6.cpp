class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
        {
            return false;
        }

        int m[26] = {0};
        for (char c : s)
        {
            m[c - 'a']++;
        }
        for (char c : t)
        {
            m[c - 'a']--;
        }
        for (int i = 0; i < 26; i++)
        {
            if (m[i])
            {
                return false;
            }
        }
        return true;
    }
};
