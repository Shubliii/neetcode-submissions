class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Logic:
        # 1. Scan the sorted array using r.
        # 2. Add an element only if it is unique.
        # 3. Store unique elements in k.
        # 4. Copy k back to nums.
        # 5. Return the count of unique elements.
        k = []

        r = 0

        while r < len(nums):

            if not k or k[-1] != nums[r]:
                k.append(nums[r])

            r += 1

        for i in range(len(k)):
            nums[i] = k[i]
        return len(k)                   



        