class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        mapSP = {}  # word -> pattern
        mapPS = {}  # pattern -> word

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            word = words[i]

            # pattern -> word
            if p in mapPS:
                if mapPS[p] != word:
                    return False
            else:
                mapPS[p] = word

            # word -> pattern
            if word in mapSP:
                if mapSP[word] != p:
                    return False
            else:
                mapSP[word] = p

        return True