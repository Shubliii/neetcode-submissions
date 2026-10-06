class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # First place all even numbers, then all odd numbers
        stack = [0] * len(nums)

        p = 0
        i = 0

        # Put even numbers first
        while p < len(nums):
            if nums[p] % 2 == 0:
                stack[i] = nums[p]
                i += 1
            p += 1

        p = 0

        # Put odd numbers after even numbers
        
        while p < len(nums):
            if nums[p] % 2 != 0:
                stack[i] = nums[p]
                i += 1
            p += 1

        return stack


        