// Last updated: 6/4/2026, 6:37:39 PM
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> hashMap = {
            {'}','{'},
            {']','['},
            {')','('}
            };
        stack<int> Stack;
        for(int i=0; i < s.length(); i++)
        {
            if(hashMap.find(s[i]) != hashMap.end())
            {
                if (!Stack.empty() && Stack.top() == hashMap[s[i]])
                    Stack.pop();
                else
                    return false;
            }
            else{
                Stack.push(s[i]);
            }
        }
        return true ? Stack.empty() : false;
    }
};