class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        
        // Iterate from the least significant digit to the most significant digit
        for (int i = n - 1; i >= 0; i--) {
            // Increment the current digit
            digits[i]++;
            
            // If the digit becomes 10, set it to 0 and carry 1 to the next iteration
            if (digits[i] == 10) {
                digits[i] = 0;
            } else {
                // If the digit is less than 10, no need to carry, break the loop
                return digits;
            }
        }
        
        // If we reach here, it means there is a carry to the most significant digit
        int[] result = new int[n + 1];
        result[0] = 1; // Set the most significant digit to 1
        return result;
    }
}
