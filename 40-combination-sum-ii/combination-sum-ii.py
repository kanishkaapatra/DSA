
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate candidates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to explore larger numbers
                if total + candidates[i] > target:
                    break

                current.append(candidates[i])

                # i + 1 ensures each element is used only once
                backtrack(i + 1, current, total + candidates[i])

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)
        return result
