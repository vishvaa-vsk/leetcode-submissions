// Last updated: 6/4/2026, 6:36:17 PM
class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        String wordsArray[] = s.split(" ");
        int len = wordsArray.length;
        String lastWord = wordsArray[len-1];
        return lastWord.length();
    }
}