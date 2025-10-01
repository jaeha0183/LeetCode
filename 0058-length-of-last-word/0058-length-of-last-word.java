class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1; // start from the last character
        int len = 0;            // length of the last word

        // skip trailing spaces
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        // count characters until we hit a space or the beginning
        while (i >= 0 && s.charAt(i) != ' ') {
            len++;
            i--;
        }

        return len; // return the length of the last word
    }
}
