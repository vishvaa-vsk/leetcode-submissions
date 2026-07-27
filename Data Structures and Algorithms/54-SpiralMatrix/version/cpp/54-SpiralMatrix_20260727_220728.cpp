// Last updated: 27/07/2026, 22:07:28
1class Solution {
2public:
3    bool isValid(string s) {
4        stack<int> st;
5
6        for(int i =0; i < s.length(); i++)
7        {
8            char ch = s[i];
9
10            if ( ch == '(' || ch == '{' || ch == '[' )
11            {
12                st.push(ch);
13            }
14            else
15            {
16                if(st.empty() || (st.top() == '(' && s[i] != ')') || (st.top() == '{' && s[i] != '}') || (st.top() == '[' && s[i] != ']'))
17                    return false;
18
19                st.pop();
20            }
21
22        }
23        return st.empty();
24    }
25};