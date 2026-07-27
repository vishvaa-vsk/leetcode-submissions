// Last updated: 27/07/2026, 20:27:56
1class Solution {
2public:
3    vector<int> spiralOrder(vector<vector<int>>& matrix) {
4        int m = matrix.size();
5        int n = matrix[0].size();
6        int top = 0 , bottom = m - 1, left = 0, right = n - 1;
7
8        vector<int> res;
9
10        while(top <= bottom && left <= right)
11        {
12            for(int i= left; i <= right; i++)
13            {
14                res.push_back(matrix[top][i]);
15            }
16            top++;
17
18            for(int i = top; i <= bottom; i++)
19            {
20                res.push_back(matrix[i][right]);
21            }
22            right-- ;
23
24            if(top <= bottom)
25            {
26                for(int i = right; i >= left; i--)
27                {
28                    res.push_back(matrix[bottom][i]);
29                }
30                bottom-- ;
31            }
32            if(left <= right){
33                for(int i = bottom; i >= top; i--)
34                {
35                    res.push_back(matrix[i][left]);
36                }
37                left++ ;
38            }
39            
40        }
41        return res;
42    }  
43};