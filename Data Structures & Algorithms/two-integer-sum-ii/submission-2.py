class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Logic:
# Use two pointers: l at the beginning and r at the end.
# Since the array is sorted:
# - If sum == target, return the 1-based indices.
# - If sum < target, move l forward to increase the sum.
# - If sum > target, move r backward to decrease the sum.

        l = 0
        r = len(numbers) - 1

        while l < r:

            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]

            if total < target:
                l += 1
            else:
                r -= 1




