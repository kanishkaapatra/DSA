class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        combination = []

        def backtrack(index):
            # A letter has been chosen for every digit
            if index == len(digits):
                result.append("".join(combination))
                return

            # Try every letter mapped to the current digit
            for letter in phone[digits[index]]:
                combination.append(letter)

                backtrack(index + 1)

                # Undo the choice before trying another letter
                combination.pop()

        backtrack(0)
        return result