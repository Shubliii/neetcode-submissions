class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l = 0
        r = len(nums) - 1

        rst = [0] * len(nums)

        # Fill result from right to left
        for i in range(len(nums) - 1, -1, -1):

            if abs(nums[l]) > abs(nums[r]): ##abs - to +
                rst[i] = nums[l] ** 2
                l += 1
            else:
                rst[i] = nums[r] ** 2
                r -= 1

        return rst         

        


