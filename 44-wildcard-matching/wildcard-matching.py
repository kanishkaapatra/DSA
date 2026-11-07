
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0

        star = -1
        match = 0

        while i < len(s):

            # Characters match or pattern has '?'
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1

            # Remember the position of '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Use the previous '*' to match one more character
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # No possible match
            else:
                return False

        # Ignore remaining '*' characters
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
