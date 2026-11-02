
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # No need to check larger candidates
                if total + num > target:
                    break

                current.append(num)

                # i instead of i + 1 allows reuse
                backtrack(i, current, total + num)

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)

        return result
