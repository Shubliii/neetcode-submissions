class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        stack=[]

        p=0

        while p<len(nums):
            if nums[p]>0:
                stack.append(nums[p])
            p+=1

        p=0

        while p<len(nums):
            if nums[p]<1:
                stack.append(nums[p])
            p+=1


        for i in range(len(stack)):
            nums[i]=stack[i]

        return nums            

        