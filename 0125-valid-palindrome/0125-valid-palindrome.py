class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # goal: keep alphanumerics only, lowercase, check front == back
        # constraints: len(s) <= 2*10^5, printable ASCII -> need O(n)

        # approach: two pointers(no new string -> O(1) space)
        #   1. left = 0, right = len-1
        #   2. skip if not alnum
        #   3. compare lower() -> False on mismatch
        #   4. step both inward

        # edge: " " -> True, ".,!" -> True, (all skipped = empty string)
        # careful: skip loops need left < right guard (IntdexError)
        left = 0
        right = len(s) - 1


        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

