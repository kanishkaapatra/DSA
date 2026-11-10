
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            # A complete permutation is formed
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose the number
                current.append(nums[i])
                used[i] = True

                # Explore further
                backtrack()

                # Undo the choice
                current.pop()
                used[i] = False

        backtrack()
        return result
