class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            result = ""
            i = 0

            while i < len(current):
                count = 1

                while i + count < len(current) and current[i] == current[i + count]:
                    count += 1

                result += str(count) + current[i]

                i += count

            current = result

        return current