class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left = []
        equal = []
        right = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])

            elif nums[i] == pivot:
                equal.append(nums[i])

            else:
                right.append(nums[i])

        return left + equal + right
        