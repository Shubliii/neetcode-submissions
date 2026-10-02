class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = []

        r = 0

        while r < len(nums):

            if not k or k[-1] != nums[r]:
                k.append(nums[r])

            r += 1

        for i in range(len(k)):
            nums[i] = k[i]
        return len(k)                   



        