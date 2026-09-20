class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = {}

        # count each character in magazine

        for char in magazine:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # use characters for ransomNote
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1

        return True