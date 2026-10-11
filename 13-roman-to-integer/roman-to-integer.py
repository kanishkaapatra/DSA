class Solution:
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            current = values[s[i]]

            # If the current value is smaller than the next,
            # subtract it; otherwise, add it.
            if i + 1 < len(s) and current < values[s[i + 1]]:
                total -= current
            else:
                total += current

        return total