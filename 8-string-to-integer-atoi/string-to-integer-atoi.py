class Solution:
    def myAtoi(self, s):
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine the sign
        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Check overflow before result * 10 + digit
            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result