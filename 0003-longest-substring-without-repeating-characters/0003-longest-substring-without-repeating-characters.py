class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Remove characters until there is no duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
        
            # Add current character and update max length
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len