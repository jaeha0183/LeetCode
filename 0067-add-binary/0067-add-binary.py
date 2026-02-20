class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # sum = a_bit + b_bit + carry
        # result_bit = sum % 2
        # carry = sum // 2

        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            carry = total // 2
            result.append(str(total % 2))
        
        return ''.join(reversed(result))
