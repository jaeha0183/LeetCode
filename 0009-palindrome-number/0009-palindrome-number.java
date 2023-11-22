class Solution {
    public boolean isPalindrome(int x) {
        // Check if x is negative or ends with 0 (except for 0 itself)
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversed = 0;
        int original = x;

        // Reverse the second half of the number
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }

        // If the original number is equal to the reversed number, it's a palindrome
        return original == reversed;
    }
}
