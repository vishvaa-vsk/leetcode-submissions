// Last updated: 6/4/2026, 6:37:58 PM
class Solution {
    public String intToRoman(int num) {
        int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String s[]= {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int i=0;
        String str = new String();
        while( num >0)
        {
            if(num>=numerals[i])
            {
                str=str+s[i];
                num-=numerals[i];
            }
            else
                i++;

        }
        return str;
    }
}