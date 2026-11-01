
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            next_result = []
            i = 0

            while i < len(result):
                count = 1

                # Count consecutive identical digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1

                # Append count followed by the digit
                next_result.append(str(count))
                next_result.append(result[i])

                i += 1

            result = "".join(next_result)

        return result
