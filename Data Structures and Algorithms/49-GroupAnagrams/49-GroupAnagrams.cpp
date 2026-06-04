// Last updated: 6/4/2026, 6:36:45 PM
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> ans;
        for(string& s: strs)
        {
            string key = s;
            sort(key.begin(),key.end());
            ans[key].emplace_back(s);
        }
        vector<vector<string>> result;
        for( auto entry: ans)
        {
            result.emplace_back(entry.second);
        }
        return result;
    }
};