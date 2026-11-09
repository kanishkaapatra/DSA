
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            # Maximum index reachable so far
            farthest = max(farthest, i + nums[i])

            # End of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # We have reached the last index
                if current_end >= len(nums) - 1:
                    break

        return jumps
