class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count=0

        for i in range(len(nums) -1):
            if(nums[i]==nums[i+1]):
                count+=1
            else:
                continue


        
        if(count>=1):
            return True
        return False